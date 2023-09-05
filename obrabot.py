import logging
from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

API_TOKEN = '6180203741:AAFNQGOji7EIcmVbtNa6KVQOBfpuc5U7QH8'

WEBHOOK_HOST = 'https://20c2-84-18-96-250.ngrok-free.app'
WEBHOOK_PATH = ''
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '127.0.0.1'
WEBAPP_PORT = 8000

'''
HOST - адрес сервера, forwarding в ngrok
URL - адрес на который будут приниматься запросы
PATH - путь до api
APP-HOST - хост приложения, локальный localhost
APP_port - порт приложения
'''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    logging.warning('Bye!')


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    return SendMessage(message.chat.id, message.text)


@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
    return SendMessage(message.chat.id, 'Вы обратились к справке бота')


@dp.message_handler(text='Hi')
async def cmd_test1(message: types.Message):
    await message.reply(f'Hi {message.from_user.username}')


@dp.message_handler(content_types=['photo'])
async def downloading(message: types.Message):
    await message.photo[-1].download(destination=r"C:\Users\rails\Desktop\table\phoic")

@dp.message_handler()
async def echo(message: types.Message):
    return SendMessage(message.chat.id, message.text)


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
