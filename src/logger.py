import logging
import os
from datetime import datetime

# Define log file name with current date and time
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

# Define the directory path for logs
logs_dir = os.path.join(os.getcwd(), "logs")

# Debug: Print the current working directory and logs directory
print(f"Current working directory: {os.getcwd()}")
print(f"Logs directory: {logs_dir}")

# Create the logs directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Check if the directory was created
if os.path.exists(logs_dir):
    print(f"Logs directory created: {logs_dir}")
else:
    print(f"Failed to create logs directory: {logs_dir}")

# Define the full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format=f"[%(asctime)s] - %(lineno)d - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)



if __name__ == "__main__":
    logging.info("Logging has started")