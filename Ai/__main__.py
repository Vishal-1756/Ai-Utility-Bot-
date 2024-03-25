from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import datetime
from Ai import bot, GROUP_ID
from Ai import get_readable_time, StartTime
import pyrogram



restart_text = """
Hue @{} I Back To Work Again

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
    start_time = time.time()    
    
    if query.data == "server":
        end_time = time.time()
        ping_time = round((end_time - start_time) * 1000, 3)
        uptime = get_readable_time((time.time() - StartTime))
    
        await query.answer(text="✨ Service Information ✨\n⏱️ Ping Time: {}ms\n🔺 Uptime: {}".format(ping_time, uptime), show_alert=True)
    else:
        pass

async def run_clients():
    await bot.start()
    await pyrogram.idle()
    zone = await get_date_time()
    await bot.send_photo(
        chat_id=GROUP_ID,
        photo="https://telegra.ph/file/0f3564033eb45dd7d5cce.jpg",
        caption=restart_text.format((await bot.get_me()).username, zone["date"], zone["time"]),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("👨‍💻 Server 👨‍💻", callback_data="server")],
                [InlineKeyboardButton(" + Add me +", url="http://t.me/GojoAiRobot?startgroup=new")]
            ]
        )
    )

if __name__ == "__main__":
    bot.loop.run_until_complete(run_clients())
