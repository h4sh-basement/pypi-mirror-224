# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
# Copyright 2020 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ---------------------------------------------------------

import json
import numpy as np
from pathlib import Path

from typing import Any, Dict, List, Tuple, Optional

from ....constants.constants import SaveFileConstants, MLFlowHFFlavourConstants, TaskConstants, Tasks
from ....nlp_auto.model import AzuremlAutoModelForSequenceClassification
from ....nlp_auto.tokenizer import AzuremlAutoTokenizer
from ....utils.mlflow_utils import SaveMLflowModelCallback, replace_deepspeed_zero3_mlflow_pytorch_weights

import torch.nn as nn

from azureml.acft.accelerator.finetune import AzuremlFinetuneArgs, AzuremlDatasetArgs
from azureml.acft.accelerator.finetune import AzuremlTrainer
from azureml.acft.accelerator.constants import HfTrainerType
from azureml.acft.common_components import get_logger_app

from transformers.tokenization_utils_base import PreTrainedTokenizerBase
from transformers.trainer_utils import EvalPrediction
from transformers.deepspeed import is_deepspeed_zero3_enabled

import torch
from sklearn.metrics import (
    f1_score,
    accuracy_score,
    roc_auc_score,
    precision_score,
    recall_score
)

from peft import TaskType


logger = get_logger_app(__name__)


class MultiLabelFinetune:

    def __init__(self, finetune_params: Dict[str, Any], dataset_class) -> None:
        # finetune params is finetune component args + args saved as part of preprocess
        self.finetune_params = finetune_params
        self.dataset_class = dataset_class
        self.ft_config = finetune_params.get("finetune_config", {})

        logger.info(f"Task name: {Tasks.MULTI_LABEL_CLASSIFICATION}")

        # Load class names
        class_names_load_path = Path(self.finetune_params["preprocess_output"], SaveFileConstants.CLASSES_SAVE_PATH)
        with open(class_names_load_path, 'r') as rptr:
            self.finetune_params["class_names"] = json.load(rptr)[SaveFileConstants.CLASSES_SAVE_KEY]
            self.finetune_params["num_labels"] = len(self.finetune_params["class_names"])

        # set log_metrics_at_root=False to not to log to parent
        self.finetune_params["log_metrics_at_root"] = True

    def _get_finetune_args(self, model_type: str) -> AzuremlFinetuneArgs:

        self.finetune_params["model_type"] = model_type
        self.finetune_params["peft_task_type"] = TaskType.SEQ_CLS
        azml_trainer_finetune_args = AzuremlFinetuneArgs(
            self.finetune_params,
            trainer_type=HfTrainerType.DEFAULT,
        )

        return azml_trainer_finetune_args

    def _get_dataset_args(self, tokenizer: Optional[PreTrainedTokenizerBase] = None) -> AzuremlDatasetArgs:

        encoded_train_ds = self.dataset_class(
            Path(self.finetune_params["preprocess_output"], self.finetune_params["encoded_train_data_fname"]),
            tokenizer=tokenizer
        )
        encoded_validation_ds = self.dataset_class(
            Path(self.finetune_params["preprocess_output"], self.finetune_params["encoded_validation_data_fname"]),
        )
        azml_trainer_dataset_args = AzuremlDatasetArgs(
            train_dataset=encoded_train_ds.dataset,
            validation_dataset=encoded_validation_ds.dataset,
            data_collator=encoded_train_ds.get_collation_function()
        )

        return azml_trainer_dataset_args

    def _load_model(self) -> Tuple[nn.Module, str, List[str]]:

        class_names = self.finetune_params["class_names"]
        id2label = {idx: lbl for idx, lbl in enumerate(class_names)}
        label2id = {lbl: idx for idx, lbl in enumerate(class_names)}
        model_params = {
            "problem_type": "multi_label_classification",
            "num_labels": self.finetune_params["num_labels"],
            "id2label": id2label,
            "label2id": label2id,
            "ignore_mismatched_sizes": self.finetune_params["ignore_mismatched_sizes"],
            "resume_from_checkpoint": self.finetune_params["resume_from_checkpoint"],
            "load_in_8bit": self.finetune_params["finetune_in_8bit"],
            "load_in_4bit": self.finetune_params["finetune_in_4bit"],
        }

        model_params.update(self.ft_config.get("load_model_kwargs", {}))
        model_params.update({"load_config_kwargs": self.ft_config.get("load_config_kwargs", {})})
        logger.info(f"Loading model with following args: {model_params}")

        model, model_type, new_initalized_layers = AzuremlAutoModelForSequenceClassification.from_pretrained(
            self.finetune_params["model_name_or_path"], **model_params)

        return model, model_type, new_initalized_layers

    def _get_tokenizer(self) -> PreTrainedTokenizerBase:
        """This method loads the tokenizer as is w/o any modifications to it"""

        tokenizer_params = {
            "apply_adjust": False,
            "task_name": self.finetune_params["task_name"],
        }

        tokenizer_params.update(self.ft_config.get("load_tokenizer_kwargs", {}))
        tokenizer_params.update({"load_config_kwargs": self.ft_config.get("load_config_kwargs", {})})
        logger.info(f"Loading tokenizer with following params: {tokenizer_params}")

        return AzuremlAutoTokenizer.from_pretrained(self.finetune_params["preprocess_output"], **tokenizer_params)

    def finetune(self) -> None:

        # configure MLflow save callback
        mlflow_infer_params_file_path = Path(
            self.finetune_params["preprocess_output"], MLFlowHFFlavourConstants.INFERENCE_PARAMS_SAVE_NAME_WITH_EXT
        )
        save_mlflow_callback = SaveMLflowModelCallback(
            mlflow_infer_params_file_path=mlflow_infer_params_file_path,
            mlflow_model_save_path=self.finetune_params["mlflow_model_folder"],
            pytorch_model_save_path=(
                self.finetune_params["pytorch_model_folder"]
                if self.finetune_params["apply_lora"] else
                None
            ),
            mlflow_task_type=self.finetune_params["mlflow_task_type"],
            class_names=self.finetune_params["class_names"],
            model_name=self.finetune_params["model_name"],
            model_name_or_path=self.finetune_params["model_name_or_path"],
            **{
                "mlflow_hf_args": {
                    "hf_config_class": "AutoConfig",
                    "hf_tokenizer_class": "AutoTokenizer",
                    "hf_pretrained_class": "AutoModelForSequenceClassification",
                },
                "mlflow_ft_conf": self.ft_config.get("mlflow_ft_conf", {}),
            },
        )

        model, model_type, new_initialized_params = self._load_model()
        tokenizer = self._get_tokenizer()
        trainer = AzuremlTrainer(
            finetune_args=self._get_finetune_args(model_type),
            dataset_args=self._get_dataset_args(tokenizer),
            model=model,
            tokenizer=tokenizer,
            metric_func=multi_label_metrics_func,
            new_initalized_layers=new_initialized_params,
            custom_trainer_callbacks=[save_mlflow_callback],
        )

        # Torch barrier is used to complete the training on a distributed setup
        # Use callbacks for adding steps to be done at the end of training
        # NOTE Avoid adding any logic after trainer.train()
        # Test the distributed scenario in case you add any logic beyond trainer.train()
        trainer.train()

        # replace pytorch weights for lora / deep speed zero3 optimization
        if trainer.should_save and is_deepspeed_zero3_enabled():
            logger.info("Replacing dummy MLflow weights ")
            replace_deepspeed_zero3_mlflow_pytorch_weights(
                self.finetune_params["pytorch_model_folder"],
                self.finetune_params["mlflow_model_folder"]
            )

        # save files only once by Rank-0 process
        if trainer.should_save:
            # save finetune args
            Path(self.finetune_params["pytorch_model_folder"]).mkdir(exist_ok=True, parents=True)
            finetune_args_path = Path(self.finetune_params["pytorch_model_folder"], \
                SaveFileConstants.FINETUNE_ARGS_SAVE_PATH)
            self.finetune_params["model_name_or_path"] = str(self.finetune_params["model_name_or_path"])
            with open(finetune_args_path, 'w') as rptr:
                json.dump(self.finetune_params, rptr, indent=2)
            # save the classes list for azmlft inference compatability
            classes_save_path = Path(self.finetune_params["pytorch_model_folder"], SaveFileConstants.CLASSES_SAVE_PATH)
            class_names_json = {SaveFileConstants.CLASSES_SAVE_KEY: self.finetune_params["class_names"]}
            with open(classes_save_path, "w") as wptr:
                json.dump(class_names_json, wptr)
            logger.info(f"Classes file saved at {classes_save_path}")


def multi_label_metrics_func(eval_pred: EvalPrediction) -> Dict[str, Any]:
    """
    compute and return metrics for sequence classification
    # source: https://jesusleal.io/2021/04/21/Longformer-multilabel-classification/
    """

    predictions, labels = eval_pred
    # first, apply sigmoid on predictions which are of shape (batch_size, num_labels)
    sigmoid = torch.nn.Sigmoid()
    probs = sigmoid(torch.Tensor(predictions))
    # next, use threshold to turn them into integer predictions
    y_pred = np.zeros(probs.shape)
    y_pred[np.where(probs >= TaskConstants.MULTI_LABEL_THRESHOLD)] = 1
    # finally, compute metrics
    y_true = labels
    # NOTE `len` method is supported for torch tensor or numpy array. It is the count of elements in first dimension
    logger.info(f"Predictions count: {len(y_pred)} | References count: {len(y_true)}")
    f1_macro_average = f1_score(y_true=y_true, y_pred=y_pred, average="macro")

    try:
        roc_auc_macro = roc_auc_score(y_true, probs, average="macro")
    except Exception as e:
        logger.warning(f"Failed to compute ROC AUC score: {e}")
        roc_auc_macro = -1

    accuracy = accuracy_score(y_true, y_pred)
    precision_macro = precision_score(y_true=y_true, y_pred=y_pred, average="macro")
    recall_macro = recall_score(y_true=y_true, y_pred=y_pred, average="macro")
    # return as dictionary
    metrics = {
        "f1_macro": f1_macro_average,
        "roc_auc_macro": roc_auc_macro,
        "accuracy": accuracy,
        "precision_macro": precision_macro,
        "recall_macro": recall_macro
    }

    return metrics
