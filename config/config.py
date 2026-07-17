from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path(__file__).parent / ".env")

BASE_URL = os.getenv("BASE_URL")
USERNAME = os.getenv("APP_USERNAME")
PASSWORD = os.getenv("APP_PASSWORD")

HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
SLOW_MO = int(os.getenv("SLOW_MO", 0))
TIMEOUT = int(os.getenv("TIMEOUT", 100000))