import sys

from us_visa.exception import CustomException
from us_visa.logger import logging






class TargetValueMapping:
    
    def __init__(self):
        self.Certified: int = 0
        self.Denied: int = 1
        
    def _asdict(self):
        return self.__dict__    # {'Certified': 0, 'Denied': 1}

    
    def reverse_mapping(self):
        mapping_response = self._asdict() # This gets the dictionary {'Certified': 0, 'Denied': 1}
        return dict(zip(mapping_response.values(),mapping_response.keys()))
    
    