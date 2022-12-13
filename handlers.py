# Import library
from main import bot, dp, admin_id
from aiogram import types
from aiogram.types import Message

array_keyboard = ['Button1', 'Button2']

# Send message to admin
async def send_to_admin(dp):
	await bot.send_message(chat_id=admin_id, text="Bot start")


# Start bot using func
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	text = f'''Привет! {message.from_user.full_name} '''
	await message.answer(text=text)
