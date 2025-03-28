

from cnnClassifier import logger
from cnnClassifier.components.training_data import Training
from cnnClassifier.config.configuration import ConfigurationManager






STAGE_NAME = "Training Data Stage"


class TrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME}   started <<<<<<<<<<")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f" >>>>>>>>>> stage {STAGE_NAME}  COMPETED <<<<<<<< \n\n x===============x")
    except Exception as e:
        logger.exception(e)
        raise e