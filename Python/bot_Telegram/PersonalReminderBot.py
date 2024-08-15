import telebot
import re
from telebot import types
from telebot.async_telebot import AsyncTeleBot
import asyncio
from datetime import datetime

TOKEN = '7397639300:AAE38ZymDYMmd1AAnyw_mWNfLD4RTZwQjXY'

bot = AsyncTeleBot(TOKEN)

# function for commands /start and /help
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
	name = message.from_user.first_name
	text = f"Hello {name}! I'm PersonalReminderBot.\nI've been created with the purpose of helping you remember what you need."
	print(message.from_user.id)
	await bot.reply_to(message, text)

# validate if message is equal to command /options
def option_func(message): return message.text.lower() == "/options"

# if message is equal to /options then the function "options" will execute
@bot.message_handler(func=option_func)
async def options(message):
	markup = types.ReplyKeyboardMarkup(row_width=2)
	option1 = types.KeyboardButton('Create new reminder')
	option2 = types.KeyboardButton('See reminders')
	markup.add(option1, option2)
	await bot.send_message(message.chat.id, text="To continue please choose an option.", reply_markup=markup)

# save the data about user and the reminders
messages = []

# if message is equal to "Create new reminder" or command "/create" then it'll execute
@bot.message_handler(func=lambda message: message.text == 'Create new reminder' or message.text == '/create')
async def create_reminder(message):
	# the message (reminder) have to starts with '.r'
	await bot.reply_to(message, "Please send your reminder text starting with '.r'")

# if message is equal to "See reminders" or command "/see" than it'll execute
@bot.message_handler(func=lambda message: message.text == 'See reminders' or message.text == '/see')
async def see_reminders(message):
	# if user saved in "messages" is right now sending messages
	user_messages = [msg for msg in messages if msg['user'] == message.from_user.username]
	if user_messages:
		# build the message that will show to user
		reminders = "\n".join([f"Reminder: {msg['text']}\nDate: {msg['date']}\n" for msg in user_messages])
		await bot.reply_to(message, f"Hi {message.from_user.username}, here are your reminders:\n\n{reminders}")
	else:
		await bot.reply_to(message, f"Hi {message.from_user.username}, you haven't reminders.")

# save all pending messages
pending_messages = {}

# take a message if this starts with '.r', then save the user's id with data (username and reminder)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.r'))
async def handle_message_create(message):
	user_id = message.from_user.id
	pending_messages[user_id] = {'user': message.from_user.username, 'text': message.text[3:]}
	# finally ask the date and hour to saved
	await bot.reply_to(message, "Now send me the date and hours you want to be notified.\nFormat: day/month/year hour:min pm/am")

# if the user's id was added into "pending_messages" then continue add the date/hour into message
@bot.message_handler(func=lambda message: message.from_user.id in pending_messages)
async def handle_date_message(message):
	user_id = message.from_user.id
	if user_id in pending_messages:
		if re.match(r'^\d{1,2}/\d{1,2}/\d{4}\s+\d{1,2}:\d{2}\s+[ap]m$', message.text, re.IGNORECASE):
			pending_messages[user_id]['date'] = message.text
			messages.append(pending_messages.pop(user_id))
			await bot.reply_to(message, "The reminder has been saved.")
		else:
			await bot.reply_to(message, "Error, send me valid date and time.")

def main():
	# execute the program indefinitely
	asyncio.run(bot.infinity_polling())

if __name__ == '__main__':
	main()
