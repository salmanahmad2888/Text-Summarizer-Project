from textSummarizer.logging import logger
from textSummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage05_model_evaluation import ModelEvaluationTrainingPipeline

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

STAGE_NAME = 'MODEL TRAINER STAGE'

try:
    logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'MODEL EVALUATION STAGE'

try:
    logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e
