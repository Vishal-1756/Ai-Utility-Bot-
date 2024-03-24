from Ai import bot , barath
 
RESTART_TEXT = """
Heya {} I Back To Work Again
Date :- {}
Time :- {}
Uptime :- {}
Ping {}
"""

async def run_clients():
      await bot.start()
      zone = await get_datetime()
      await bot.send_message(
           chat_id=config.GROUP_ID,
           text=strings.RESTART_TEXT.format(date=zone["date"], time=zone["time"]))      

if __name__ == "__main__":
    bot.loop.run_until_complete(run_clients())
