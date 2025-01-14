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

from pathlib import Path
from argparse import Namespace
from typing import Dict, Any, Tuple, Optional
from dataclasses import asdict
import copy

import json

from .base import MultiLabelPreprocessArgs, MultiLabelDataset
from ....nlp_auto.config import AzuremlAutoConfig
from ....nlp_auto.tokenizer import AzuremlAutoTokenizer
from ....constants.constants import Tasks, DatasetSplit, SaveFileConstants, MLFlowHFFlavourConstants

from azureml.acft.common_components.utils.error_handling.exceptions import ACFTDataException
from azureml.acft.common_components.utils.error_handling.error_definitions import InvalidDataset, InvalidLabel
from azureml._common._error_definition.azureml_error import AzureMLError  # type: ignore
from azureml.acft.common_components import get_logger_app

from transformers.tokenization_utils_base import PreTrainedTokenizerBase


logger = get_logger_app(__name__)


class MultiLabelPreprocessForFinetune:

    def __init__(self, component_args: Namespace, preprocess_args: MultiLabelPreprocessArgs) -> None:
        # component args is combined args of
        #  - preprocess component args
        #  - model_name arg from model selector
        #  - newly constructed model_name_or_path
        self.component_args = component_args
        self.preprocess_args = preprocess_args
        self.ft_config = getattr(component_args, "finetune_config", {})

        logger.info(f"Task name: {Tasks.MULTI_LABEL_CLASSIFICATION}")

        self.model_type = AzuremlAutoConfig.get_model_type(
            hf_model_name_or_path=component_args.model_name_or_path,
            **self.ft_config.get("load_config_kwargs", {}),
        )
        logger.info(self.preprocess_args)

        self.tokenizer = self._init_tokenizer()

    def _init_tokenizer(self) -> PreTrainedTokenizerBase:
        """Initialize the tokenizer and set the model max length for the tokenizer if not already set"""

        tokenizer_params = {
            "task_name": Tasks.MULTI_LABEL_CLASSIFICATION,
            "apply_adjust": True,
            "max_sequence_length": self.preprocess_args.max_seq_length,
        }

        tokenizer_params.update(self.ft_config.get("load_tokenizer_kwargs", {}))
        tokenizer_params.update({"load_config_kwargs": self.ft_config.get("load_config_kwargs", {})})

        return AzuremlAutoTokenizer.from_pretrained(self.component_args.model_name_or_path, **tokenizer_params)

    def _get_encode_dataset_params(self) -> Dict[str, Any]:

        encode_params = {}
        # padding and truncation
        encode_params["padding"] = "max_length" if self.preprocess_args.pad_to_max_length else False
        encode_params["truncation"] = True

        # max sequence length
        if self.preprocess_args.max_seq_length == -1:
            self.preprocess_args.max_seq_length = self.tokenizer.model_max_length
        encode_params["max_length"] = min(self.preprocess_args.max_seq_length, self.tokenizer.model_max_length)

        # returns all the scores of multi label model
        encode_params["return_all_scores"] = True

        return encode_params

    def _save_raw_data(self) -> Tuple[str, str, Optional[str]]:
        # save the raw train and valid dataset
        # NOTE call this function before encoding the dataset else this will save encoded datasaet
        logger.info("Saving the raw datasets")
        raw_folder_name = "raw_data"
        raw_data_save_folder = str(Path(self.component_args.output_dir, raw_folder_name))
        raw_train_data_fname = str(
            Path(
                raw_folder_name,
                self.train_ds.save(
                    save_folder=raw_data_save_folder,
                    save_name=DatasetSplit.TRAIN,
                    batch_size=self.preprocess_args.batch_size
                )
            )
        )
        raw_validation_data_fname = str(
            Path(
                raw_folder_name,
                self.valid_ds.save(
                    save_folder=raw_data_save_folder,
                    save_name=DatasetSplit.VALIDATION,
                    batch_size=self.preprocess_args.batch_size
                )
            )
        )
        raw_test_data_fname = None
        if self.test_ds is not None:
            raw_test_data_fname = str(
                Path(
                    raw_folder_name,
                    self.test_ds.save(
                        save_folder=raw_data_save_folder,
                        save_name=DatasetSplit.TEST,
                        batch_size=self.preprocess_args.batch_size
                    )
                )
            )

        return (raw_train_data_fname, raw_validation_data_fname, raw_test_data_fname)

    def _load_data_splits(self, save_raw_data: bool = False) -> Optional[Tuple[str, str, str]]:
        """
        1. Load train, validation and test data splits
        2. Add column prefix for the data
        """
        # encode params used for encoding dataset
        self.encode_params = self._get_encode_dataset_params()

        # initialize dataset
        dataset_args=asdict(self.preprocess_args)
        dataset_args.update(self.encode_params)
        kwargs = dict(
            dataset_args=dataset_args,
            required_columns=self.preprocess_args.required_columns,
            required_column_dtypes=self.preprocess_args.required_column_dtypes,
            label_column=self.preprocess_args.label_column,
            tokenizer=self.tokenizer,
        )
        logger.info("Loading train dataset")
        self.train_ds = MultiLabelDataset(
            self.component_args.train_data_path,
            **copy.deepcopy(kwargs),
            slice=self.component_args.train_slice,
        )
        # decode the old label column and populate the new one
        self.train_ds.dataset = self.train_ds.dataset.map(
            self.train_ds.decode_label_column,
            batched=True,
            batch_size=self.preprocess_args.batch_size,
            writer_batch_size=self.preprocess_args.batch_size
        )
        logger.info("Loading validation dataset")
        self.valid_ds = MultiLabelDataset(
            self.component_args.validation_data_path,
            **copy.deepcopy(kwargs),
            slice=self.component_args.validation_slice,
        )
        # decode the old label column and populate the new one
        self.valid_ds.dataset = self.valid_ds.dataset.map(
            self.valid_ds.decode_label_column,
            batched=True,
            batch_size=self.preprocess_args.batch_size,
            writer_batch_size=self.preprocess_args.batch_size
        )
        if self.component_args.test_data_path is not None:
            logger.info("Loading test dataset")
            self.test_ds = MultiLabelDataset(
                self.component_args.test_data_path,
                **copy.deepcopy(kwargs),
                label_column_optional=False,
                slice=self.component_args.test_slice,
            )
            # decode the old label column and populate the new one
            self.test_ds.dataset = self.test_ds.dataset.map(
                self.test_ds.decode_label_column,
                batched=True,
                batch_size=self.preprocess_args.batch_size,
                writer_batch_size=self.preprocess_args.batch_size
            )
        else:
            self.test_ds = None

        # save raw data
        if save_raw_data:
            (
                raw_train_data_fname,
                raw_validation_data_fname,
                raw_test_data_fname
            ) = self._save_raw_data()

        # add dataset prefix
        self.train_ds.update_dataset_columns_with_prefix()
        self.train_ds.update_required_columns_with_prefix()
        self.valid_ds.update_dataset_columns_with_prefix()
        self.valid_ds.update_required_columns_with_prefix()
        if not self.component_args.skip_test_data_processing and self.test_ds is not None:
            self.test_ds.update_dataset_columns_with_prefix()
            self.test_ds.update_required_columns_with_prefix()

        if save_raw_data:
            return (raw_train_data_fname, raw_validation_data_fname, raw_test_data_fname)

    def _validate_data_splits(self):
        """
        1. validate the datasets
        2. Identify the classnames and do some validations on them
        """
        # validate the datasets
        logger.info("Validating the train dataset")
        self.train_ds.validate()
        logger.info("Validating the validation dataset")
        self.valid_ds.validate()
        if not self.component_args.skip_test_data_processing and self.test_ds is not None:
            logger.info("Validating the test dataset")
            self.test_ds.validate()

        # Identify the class names - combination of train and validation datasets
        # class names are list of strings
        self.class_names_train_plus_valid = sorted(set(self.train_ds.class_names + self.valid_ds.class_names))  # type: ignore
        # few classes to do classification
        if len(self.class_names_train_plus_valid) < 2:
            raise ACFTDataException._with_error(AzureMLError.create(InvalidDataset))
        logger.info(f"Identified class names: {self.class_names_train_plus_valid}")
        if not self.component_args.skip_test_data_processing and self.test_ds is not None:
            self.class_names_test= self.test_ds.class_names
            # test ds has extra classes that are not in train and valid
            test_ds_extra_labels = set(self.class_names_test).difference(set(self.class_names_train_plus_valid))  # type: ignore
            if test_ds_extra_labels:
                raise ACFTDataException._with_error(AzureMLError.create(InvalidLabel, label=test_ds_extra_labels))

    def _encode_data_splits(self):
        """
        Encode the dataset
        """
        logger.info("Encoding the train dataset")
        self.train_ds.encode_dataset(class_names_train_plus_valid=self.class_names_train_plus_valid)
        self.train_ds.dataset = MultiLabelDataset.set_column_dtype(self.train_ds.dataset, "labels", to_dtype="float32")
        logger.info("Encoding the validation dataset")
        self.valid_ds.encode_dataset(class_names_train_plus_valid=self.class_names_train_plus_valid)
        self.valid_ds.dataset = MultiLabelDataset.set_column_dtype(self.valid_ds.dataset, "labels", to_dtype="float32")
        if not self.component_args.skip_test_data_processing and self.test_ds is not None:
            logger.info("Encoding the test dataset")
            self.test_ds.encode_dataset(class_names_train_plus_valid=self.class_names_train_plus_valid)
            self.test_ds.dataset = MultiLabelDataset.set_column_dtype(self.test_ds.dataset, "labels", to_dtype="float32")

    def preprocess(self) -> None:
        """
        Preprocess the raw dataset
        """

        # load, validate and encode the datasets
        (
            raw_train_data_fname,
            raw_validation_data_fname,
            raw_test_data_fname
        ) = self._load_data_splits(save_raw_data=True)
        self._validate_data_splits()
        self._encode_data_splits()

        # Save
        # 1. encoded datasets
        # 2. Arguments
        # 3. class names
        # 4. tokenizer
        # 5. mlflow inference data

        # 1. Encoded datasets
        logger.info("Saving the encoded datasets")
        encoded_train_data_fname = self.train_ds.save(
            save_folder=self.component_args.output_dir,
            save_name=DatasetSplit.TRAIN,
            batch_size=self.preprocess_args.batch_size
        )
        encoded_validation_data_fname = self.valid_ds.save(
            save_folder=self.component_args.output_dir,
            save_name=DatasetSplit.VALIDATION,
            batch_size=self.preprocess_args.batch_size
        )
        if not self.component_args.skip_test_data_processing and self.test_ds is not None:
            encoded_test_data_fname = self.test_ds.save(
                save_folder=self.component_args.output_dir,
                save_name=DatasetSplit.TEST,
                batch_size=self.preprocess_args.batch_size
            )

        # 2. Arguments: save the preprocess args, model_type, encoded datasets
        preprocess_args = vars(self.component_args)
        preprocess_args.update(vars(self.preprocess_args))
        # add the model path
        preprocess_args["model_type"] = self.model_type
        # add the paths for raw train, validation and test paths
        preprocess_args["raw_train_data_fname"] = raw_train_data_fname
        preprocess_args["raw_validation_data_fname"] = raw_validation_data_fname
        # Only processing the test data is controlled using the flag; we will still save the raw dataset for test
        if self.test_ds is not None:
            preprocess_args["raw_test_data_fname"] = raw_test_data_fname
        # add the paths for encoded train, validation and test paths
        preprocess_args["encoded_train_data_fname"] = encoded_train_data_fname
        preprocess_args["encoded_validation_data_fname"] = encoded_validation_data_fname
        if not self.component_args.skip_test_data_processing and self.test_ds is not None:
            preprocess_args["encoded_test_data_fname"] = encoded_test_data_fname
        preprocess_args_save_path = Path(self.component_args.output_dir, SaveFileConstants.PREPROCESS_ARGS_SAVE_PATH)
        preprocess_args["model_name_or_path"] = str(preprocess_args["model_name_or_path"])
        logger.info(f"Saving the preprocess args to {preprocess_args_save_path}")
        with open(preprocess_args_save_path, 'w') as fp:
            json.dump(preprocess_args, fp, indent=2)

        # 3. class names
        class_names_save_path = Path(self.component_args.output_dir, SaveFileConstants.CLASSES_SAVE_PATH)
        logger.info(f"Saving the class names to {class_names_save_path}")
        class_names_data = {
            SaveFileConstants.CLASSES_SAVE_KEY: self.class_names_train_plus_valid
        }
        with open(class_names_save_path, 'w') as fp:
            json.dump(class_names_data, fp, indent=2)

        # 4. tokenizer
        self.tokenizer.save_pretrained(self.component_args.output_dir)

        # 5. save the mlflow inference params
        save_key = MLFlowHFFlavourConstants.INFERENCE_PARAMS_SAVE_KEY
        save_data = {
            save_key: self.encode_params
        }
        mlflow_inference_params_save_path = Path(
            self.component_args.output_dir, MLFlowHFFlavourConstants.INFERENCE_PARAMS_SAVE_NAME_WITH_EXT)
        logger.info(f"Saving the mlflow inference params at {mlflow_inference_params_save_path}")
        with open(mlflow_inference_params_save_path, 'w') as wptr:
            json.dump(save_data, wptr)
