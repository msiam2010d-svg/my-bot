import os, telebot
from telebot import types
BOT_TOKEN=os.environ.get("BOT_TOKEN")
ADSTERRA_LINK="https://auctionr.org/4/7c43e9bddd"
bot=telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start'])
def start(m):
 bot.send_message(m.chat.id,"Hi! Link pathao")
@bot.message_handler(func=lambda m:True)
def handle(m):
 markup=types.InlineKeyboardMarkup()
 markup.add(types.InlineKeyboardButton(text="1. Watch Ad",url=ADSTERRA_LINK))
 markup.add(types.InlineKeyboardButton(text="2. Verify",callback_data="verify"))
 bot.send_message(m.chat.id,"Download pete 1 e click koro",reply_markup=markup)
@bot.callback_query_handler(func=lambda c:True)
def verify(c):
 bot.send_message(c.message.chat.id,"Verified!")
bot.infinity_polling()
