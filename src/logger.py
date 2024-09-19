import logging
import os
from datetime import datetime

# Create the log file name with the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the log directory (without the log file name)
log_dir = os.path.join(os.getcwd(), "Logs")

# Create the Logs directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Configure the logging settings with correct placeholders
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Correct format placeholders
    level=logging.INFO,
)

# Main block to start logging
# if __name__ == "__main__":
#     logging.info('Logging has started.')
