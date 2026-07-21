import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    BASE_URL = os.getenv("BASE_URL")

    USERNAME = os.getenv("APP_USERNAME")

    PASSWORD = os.getenv("APP_PASSWORD")

    TIMEOUT = int(os.getenv("TIMEOUT"))
    
    SLOW_MO = int(os.getenv("SLOW_MO", 0))

    HEADLESS = os.getenv("HEADLESS").lower() == "true"