from textSummarizer.logging import logger
from textSummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline

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

STAGE_NAME = 'DATA VALIDATION STAGE'

try:
    logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'DATA TRANSFORMATION STAGE'

try:
    logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e
