from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import datetime
from Ai import bot, GROUP_ID
from Ai import get_readable_time


start_time = time.time()    
end_time = time.time()
ping_time = round((end_time - start_time) * 1000, 3)
uptime = get_readable_time((time.time() - StartTime))
    
   
restart_text = """
Heya {} I'm Back To Work Again
Date: {}
Time: {}
"""

async def get_date_time():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    return {"date": date, "time": time}

@bot.on_callback_query()
async def callback_handler(bot, query):
    if query.data == "server":
        await query.answer(text="✨ Service Information ✨\n⏱️ Ping Time: {}ms\n🔺 Uptime: {}".format(ping_time, uptime), show_alert=True)
    else:
        pass

async def run_clients():
    await bot.start()
    zone = await get_date_time()
    await bot.send_message(
        chat_id=GROUP_ID,
        text=restart_text.format((await bot.get_me()).username, zone["date"], zone["time"]),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("👨‍💻 Server 👨‍💻", callback_data="server")],
                [InlineKeyboardButton(" + Add me +", url="http://t.me/VegetaRobot?startgroup=new")]
            ]
        )
    )

if __name__ == "__main__":
    bot.loop.run_until_complete(run_clients())
