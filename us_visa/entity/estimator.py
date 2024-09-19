import sys
from pandas import DataFrame
from us_visa.exception import CustomException
from us_visa.logger import logging
from sklearn.pipeline import Pipeline






class TargetValueMapping:
    
    def __init__(self):
        self.Certified: int = 0
        self.Denied: int = 1
        
    def _asdict(self):
        return self.__dict__    # {'Certified': 0, 'Denied': 1}

    
    def reverse_mapping(self):
        mapping_response = self._asdict() # This gets the dictionary {'Certified': 0, 'Denied': 1}
        return dict(zip(mapping_response.values(),mapping_response.keys()))
    
    
class USvisaModel:
    
    
    def __init__(self, preprocessing_object: Pipeline, trained_model_object: object):
        """
        :param preprocessing_object: Input Object of preprocesser
        :param trained_model_object: Input Object of trained model 
        """
        
        self.preprocessing_objec = preprocessing_object
        self.trained_model_object = trained_model_object
        
        
    def predict(self, dataframe: DataFrame ) -> DataFrame:
        """
        Function accepts raw inputs and then transformed raw input using preprocessing_object
        which guarantees that the inputs are in the same format as the training data
        At last it performs prediction on transformed features
        """
        
        logging.info("Entered predict method of USvisamodel class")
        
        try:
            
            logging.info("Using the trained model to get predictions")
            
            transformed_feature = self.preprocessing_objec.transform(dataframe)
            
            logging.info("Used the trained model to get prediction")
            
            return self.trained_model_object.predict(transformed_feature)
        
        
        except Exception as e:
            raise CustomException(e,sys) from e
        
        
    def __repr__(self):
        return f"{type(self.trained_model_object).__name__}()"
    
    def __str__(self) -> str:
        return f"{type(self.trained_model_object).__name__}()"
    
    