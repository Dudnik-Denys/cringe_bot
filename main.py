from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram import F
from aiogram.enums import ParseMode
from dotenv import load_dotenv, find_dotenv
import asyncio
import os

load_dotenv(find_dotenv())
bot = Bot(token=os.getenv('TOKEN'), parse_mode=ParseMode.HTML)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(text=f'Hello, {message.from_user.full_name}!')


@dp.message(Command('help'))
async def help_cmd(message: types.Message):
    await message.answer(f'Bot info')


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    asyncio.run(main())
