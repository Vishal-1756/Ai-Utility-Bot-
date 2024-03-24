from Ai import bot , barath
import time

start_time = time.time()    
end_time = time.time()
ping_time = round((end_time - start_time) * 1000, 3)
uptime = get_readable_time((time.time() - StartTime))
    
RESTART_TEXT = """
Heya {} I Back To Work Again
Date :- {}
Time :- {}
"""

async def get_date_time:

async def run_clients():
      await bot.start()
      zone = await get_date_time
      await bot.send_message(
           chat_id=config.GROUP_ID,
           text=strings.RESTART_TEXT.format(date=zone["date"], time=zone["time"]))      

if __name__ == "__main__":
    bot.loop.run_until_complete(run_clients())
