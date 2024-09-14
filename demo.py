from us_visa.pipeline.training_pipeline import TrainPipeline


obj = TrainPipeline()
obj.run_pipeline()









""" 
logging.info("Hey first world!")

try:
    a = 2/0
except Exception as e:
    logging.info(CustomException(e, sys))
    raise CustomException(e,sys) from e 
"""