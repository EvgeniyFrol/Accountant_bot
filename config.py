import os
from dotenv import load_dotenv


# Find .env file with os variables
load_dotenv(".env")

# retrieve config variables
try:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
except (TypeError, ValueError) as ex:
    print("Error while reading config:", ex)