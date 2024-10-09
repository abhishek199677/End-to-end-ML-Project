import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"  

log_dir = "logs"  #directory name

log_filepath = os.path.join(log_dir, "running_log.log") #this create a log_dir directory inside it creates a file nameed running_log.log
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level = logging.INFO,
    format = logging_str,

    handlers=[
        # logging.FileHandler(log_filepath),   #using FileHandler the message will be shown in the new created directory i.e logs
        # logging.StreamHandler(sys.stdout)    #using StreamHandler the messahge will be shown in the terminal
    ]
)

logger = logging.getLogger("mlProjectLogger")  #defining logger object