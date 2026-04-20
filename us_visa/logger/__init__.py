import logging
import os
from from_root import from_root
from datetime import datetime

# Generate the filename
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the full directory path inside the project root
logs_path = os.path.join(from_root(), 'logs')

# Create the directory (use 'makedirs')
os.makedirs(logs_path, exist_ok=True)

# Join the directory path with the filename
final_log_path = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=final_log_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)