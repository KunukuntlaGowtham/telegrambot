import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Access sensitive data
FIREBASE_CREDENTIALS_PATH = os.getenv("FIREBASE_CREDENTIALS_PATH")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
