import logging
import os

os.makedirs("reports", exist_ok=True)

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(message)s"

logging.basicConfig(

    filename="reports/automation.log",

    level=logging.INFO,

    format=LOG_FORMAT,

    filemode="w"

)

logger = logging.getLogger(__name__)