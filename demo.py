from us_visa.logger import logging
from us_visa.exception import CustomException
import sys


logging.info("Hey first world!")

try:
    a = 2/0
except Exception as e:
    logging.info(CustomException(e, sys))
    raise CustomException(e,sys) from e 