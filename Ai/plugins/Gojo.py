import requests
from pyrogram import filters, Client
from pyrogram.types import Message
from Ai import bot
import httpx

api_url_chat5 = "https://tofu-api.onrender.com/chat/gpt"

old_prompt = {}

def fetch_data(api_url: str, query: str, user_id: int) -> tuple:
    op = old_prompt.get(user_id, "")
    query = op + " " + query if op else query
    try:
        response = requests.get(f"{api_url}/{query}")
        response.raise_for_status()
        data = response.json()
        if data.get("code") == 2:
            return data.get("content", "No response from the API."), None
        else:
            return None, f"API error: {data.get('message', 'Unknown error')}"
    except requests.exceptions.RequestException as e:
        return None, f"Request error: {e}"
    except Exception as e:
        return None, f"An error occurred: {str(e)}"

@bot.on_message(filters.command(["gojo","gojoai"], prefixes=""))
async def gojo_ai(_: Client, message: Message):
    user_id = message.from_user.id
    if len(message.command) < 2:
        return await message.reply_text("**Please provide a query.**")

    query = " ".join(message.command[1:])    
    txt = await message.reply_text("**Wait patiently, requesting to API...**")
    await txt.edit("💭")
    api_response, error_message = fetch_data(api_url_chat5, query, user_id)
    old_prompt[user_id] = api_response
    await txt.edit(api_response or error_message)
    
    if txt.reply_to_message and txt.reply_to_message.from_user.id == user_id:
        # If the message was replied by the bot, generate a new response
        new_query = txt.reply_to_message.text
        api_response, error_message = fetch_data(api_url_chat5, new_query, user_id)
        old_prompt[user_id] = api_response
        await message.reply_text(api_response or error_message)
