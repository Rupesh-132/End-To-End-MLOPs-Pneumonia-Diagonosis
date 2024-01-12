from src.Pneumonia_Diagnosis import logger
from src.Pneumonia_Diagnosis.pipeline.data_ingestion_pipeline import DataIngestionPipeline


STAGE_NAME = "Data Ingestion Step"


try:
    logger.info(f"{STAGE_NAME} started ")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} \n\n x==========x")
except Exception as e:
    logger.exception(e)
    raise e
