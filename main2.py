import logging
from aiogram import Bot, types, Dispatcher, executor

API_TOKEN = '6180203741:AAFNQGOji7EIcmVbtNa6KVQOBfpuc5U7QH8'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.reply('start')


@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
    await message.reply('Справка хули')


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
