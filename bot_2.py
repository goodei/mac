from telegram.ext import Updater , CommandHandler, MessageHandler, Filters
from bot_1 import get_answer
import ephem
import datetime

"""date = datetime.datetime.now()
now_time = date.strftime('%Y.%m.%d')
def cosm(bot, update):
    print('loaded /planet')
    bot.sendMessage(update.message.chat_id , planets = input('Enter a planet you need'))
    planet = ephem.planets(now_time)
    bot.sendMessage(update.message.chat_id, ephem.constellation(planet))"""


def greet_user(bot, update):
    print('Loaded /start')
    bot.sendMessage(update.message.chat_id, text = 'Lets talk')

def show_error(bot, update, error):
    print(error)

def talk_to_me(bot, update):
        bot.sendMessage(update.message.chat_id, get_answer(update.message.text))

def bot():
    updater = Updater("353342905:AAH8q8DLhpUXPI3K-uRkxJwU4cdqLxgnRbs")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    #dp.add_handler(CommandHandler("planet", cosm))
    dp.add_error_handler(show_error)
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    #dp.add_handler(MessageHandler([Filters.text], cosm))


    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    bot()