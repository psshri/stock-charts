# import time
import json
from telegram import Bot
from telegram import InputFile
import asyncio
import nest_asyncio
nest_asyncio.apply()
# import nest_asyncio
# nest_asyncio.apply()

# start_time = time.time()

with open('../info.json', 'r') as file:
    data = json.load(file)
file.close()

bot_token = data['telegram_bot_token']
chat_id = data['telegram_chat_id']

bot = Bot(token=bot_token)

async def sendit(pdf_file_path, chat_id=chat_id, bot=bot):
    print(f'sending {pdf_file_path[17:]} ...')
    with open(pdf_file_path, 'rb') as pdf_file:
        await bot.send_document(chat_id=chat_id, document=InputFile(pdf_file), read_timeout=1000, write_timeout=1000, connect_timeout=1000, pool_timeout=1000)
    print(f'sent {pdf_file_path[17:]} ...')
    pdf_file.close()

# # pdf_file_path = 'charts/test.pdf'
# pdf_file_path_dw1 = 'ohlc-charts/PDFs/dw1.pdf'
# pdf_file_path_dw2 = 'ohlc-charts/PDFs/dw2.pdf'
# pdf_file_path_dw3 = 'ohlc-charts/PDFs/dw3.pdf'
# pdf_file_path_dw4 = 'ohlc-charts/PDFs/dw4.pdf'
# pdf_file_path_myport = 'ohlc-charts/PDFs/myport.pdf'

# loop = asyncio.get_event_loop()
# # Blocking call which returns when the display_date() coroutine is done
# loop.run_until_complete(sendit(pdf_file_path_dw1, chat_id, bot))
# loop.run_until_complete(sendit(pdf_file_path_dw2, chat_id, bot))
# loop.run_until_complete(sendit(pdf_file_path_dw3, chat_id, bot))
# loop.run_until_complete(sendit(pdf_file_path_dw4, chat_id, bot))
# loop.run_until_complete(sendit(pdf_file_path_myport, chat_id, bot))


# end_time = time.time()
# elapsed_time = end_time - start_time
# minutes = round(elapsed_time / 60, 2)
# print(f"Time taken: {minutes} minutes")