from src.Pneumonia_Diagnosis.config_manager.configuration import ConfigurationManager
from src.Pneumonia_Diagnosis.strategies.data_ingestion import DataIngestionStrategy
from src.Pneumonia_Diagnosis import logger


STAGE_NAME = "Data Ingestion Pipeline"


class DataIngestionPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestionStrategy(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f"{STAGE_NAME} started")
        data_ingestion_pipeline = DataIngestionPipeline()
        data_ingestion_pipeline.run()
        logger.info(f"stage {STAGE_NAME} completed \n\n")
    except Exception as e:
        logger.exception(e)
        raise e