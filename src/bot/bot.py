import telebot

from src.misc.config import BOT_TOKEN
from src.bot.markups import keyboards,buttons

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text = "Press button to update data in sheets",reply_markup=keyboards.home_keyboard())

@bot.message_handler(content_types=["text"])
def main_handler(message):
    if message.text == buttons.data.UPDATE_BT:
        pass
    else:
        bot.send_message(message.chat.id, text = "Sorry? I dont understand", reply_markup = keyboards.home_keyboard())

