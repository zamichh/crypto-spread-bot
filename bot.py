import asyncio
import aiohttp
from aiogram import Bot, Dispatcher

API_TOKEN = "8462385789:AAEVmK5T6AthaXaEx9ttPQj_tSjQ6Bla6Z8""
CHAT_ID = "505722260"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def get_price():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.bybit.com/v2/public/tickers?symbol=BTCUSDT") as resp:
            data = await resp.json()
            return data["result"][0]["last_price"]

async def main():
    while True:
        price = await get_price()
        await bot.send_message(CHAT_ID, f"BTC price: {price}")
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
