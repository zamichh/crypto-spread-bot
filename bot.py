import asyncio
import aiohttp
from aiogram import Bot, Dispatcher

API_TOKEN = "PUT_YOUR_TOKEN_HERE"
CHAT_ID = "PUT_YOUR_CHAT_ID_HERE"

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
