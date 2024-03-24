import os
import logging
from pyrogram import Client 
import time

FORMAT = "[INFO]: %(message)s"

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()], format=FORMAT)

StartTime = time.time()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
TOKEN = os.getenv("TOKEN")
GROUP_ID = -1001717881477

bot = Client(
       name="AI",
       api_id=API_ID,
       api_hash=API_HASH,
       bot_token=TOKEN,
       plugins=dict(root="Ai"),)
