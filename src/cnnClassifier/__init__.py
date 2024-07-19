# Logger Setup 
#- Will assist with Tracking/ Debugging

import os
import sys
import logging


# Format of logging (Includes Time, Level of Logging, Code location i.e. which module, Message/decription of the code)
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


log_dir = "logs" #Create a folder
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok = True)

# Logger setup
logging.basicConfig(
    level= logging.INFO, #Information logging logger
    format= logging_str, #Refers to defined format
   
   #Handlers required to handle the operation of logging
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Logger name
logger = logging.getLogger("cnnClassifierLogger")