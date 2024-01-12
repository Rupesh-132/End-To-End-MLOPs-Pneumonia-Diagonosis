import os
from src.Pneumonia_Diagnosis.constants import *
from src.Pneumonia_Diagnosis.utils.common import read_yaml, create_directories
from src.Pneumonia_Diagnosis.entity.entity_configuration import (DataIngestionConfig)


class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        """
        Method to set the load the config and params file and create artifacts directory
        :param config_filepath:
        :param params_filepath:
        """
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Method to create the DataIngestion configuration
        :return: DataIngestionConfig
        """
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config