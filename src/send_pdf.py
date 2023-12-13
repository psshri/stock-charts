import json
from telegram import Bot
from telegram import InputFile
import asyncio
import nest_asyncio
nest_asyncio.apply()

with open('../info.json', 'r') as file:
    data = json.load(file)
file.close()

bot_token = data['telegram_bot_token']
chat_id = data['telegram_chat_id']

timeout = 1000

bot = Bot(token=bot_token)

async def sendit(pdf_file_path, chat_id=chat_id, bot=bot):
    print(f'sending {pdf_file_path[17:]} ...')
    with open(pdf_file_path, 'rb') as pdf_file:
        await bot.send_document(chat_id=chat_id, document=InputFile(pdf_file), read_timeout=timeout, write_timeout=timeout, connect_timeout=timeout, pool_timeout=timeout)
    print(f'sent {pdf_file_path[17:]} !')
    pdf_file.close()