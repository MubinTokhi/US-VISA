import os
import logging
from datetime import datetime


# directory name
LOG_DIR = "logs"

#making directory 
os.makedirs(LOG_DIR, exist_ok=True)

# creating timeframe for the log file
LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.logs"

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= '[%(asctime)s] %(name)s - %(lineno)d - %(levelname)s - %(message)s',
    level=logging.INFO,
)