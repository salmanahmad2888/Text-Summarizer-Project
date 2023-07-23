from textSummarizer.logging import logger
from textSummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline

logger.info("Main.py: Pipeline started...")

STAGE_NAME = 'DATA INGESTION STAGE'

try:
    logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e