import os
import logging
from pyrogram import Client 
import time

FORMAT = "[INFO]: %(message)s"

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()], format=FORMAT)

StartTime = time.time()

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time



API_ID = "23659727"
API_HASH = "b8a345d0b0208c0b46c5522164de8c4f"
TOKEN = "7067552176:AAHi8JYdtMHtz1TFu4uk0K9ZPI8GW1B9H4Y"
GROUP_ID = -1001717881477

bot = Client(
       name="AI",
       api_id=API_ID,
       api_hash=API_HASH,
       bot_token=TOKEN,
       plugins=dict(root="Ai"),)
