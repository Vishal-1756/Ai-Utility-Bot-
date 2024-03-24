import requests
from pyrogram import filters, Client
from pyrogram.types import Message
from Ai import bot
import asyncio

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
    api_response, error_message = fetch_data(api_url_chat5, query, user_id)
    old_prompt[user_id] = api_response
    await message.reply_text(api_response or error_message)
    await asyncio.sleep(300)  # Clear data after 5 minutes
    if user_id in old_prompt:
        del old_prompt[user_id]

@bot.on_message(filters.reply & filters.text & ~filters.me)
async def reply_to_bot_message(client: Client, message: Message):
    user_id = message.from_user.id
    if user_id in old_prompt:
        if old_prompt[user_id] is not None:
            new_query = old_prompt[user_id] + " " + message.text
        else:
            new_query = message.text
        api_response, error_message = fetch_data(api_url_chat5, new_query, user_id)
        old_prompt[user_id] = api_response
        await message.reply_text(api_response or error_message)
        await asyncio.sleep(300)  # Clear data after 5 minutes
        if user_id in old_prompt:
            del old_prompt[user_id]
