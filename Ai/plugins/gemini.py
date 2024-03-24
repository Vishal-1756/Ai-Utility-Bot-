import requests
from pyrogram import filters, Client
from pyrogram.types import Message
from Ai import bot

api_url_chat5 = "https://tofu-api.onrender.com/chat/gemini"

def fetch_data(api_url: str, query: str) -> tuple:
    try:
        response = requests.get(f"{api_url}/{query}")
        response.raise_for_status()
        data = response.json()
        if data.get("code") == 2:
            content = data.get("content", [])
            if content:
                return content[0].get("text"), None
            else:
                return "No response from the API.", None
        else:
            return None, f"API error: {data.get('message', 'Unknown error')}"
    except requests.exceptions.RequestException as e:
        return None, f"Request error: {e}"
    except Exception as e:
        return None, f"An error occurred: {str(e)}"

@bot.on_message(filters.command(["gemini"]))
@bot.on_message(filters.command(["gemini"], prefixes=""))
async def gemini(_: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("**Please provide a query.**")

    query = " ".join(message.command[1:])    
    txt = await message.reply_text("**Wait patiently, requesting to API...**")
    await txt.edit("✨")
    api_response, error_message = fetch_data(api_url_chat5, query)
    await txt.edit(api_response or error_message)

