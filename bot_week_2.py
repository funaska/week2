# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import logging
import datetime
from secret_key import secret_key
# Настройки прокси
# PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080', 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
# PROXY = {'proxy_url': 'socks5://95.215.54.206:39880'}
PROXY = {'proxy_url': 'socks5://u0k12.tgproxy.me:1080', 'urllib3_proxy_kwargs': {'username': 'telegram', 'password': 'telegram'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='logs/bot.log'
                    )

def greet_user(bot, update):
    text = 'Привет!'
    print(text,'пользователю')
    update.message.reply_text(text)
    # print('Привет!')

def planet_to_const(bot, update):
    planet = update.message.text.split()[1]
    print('Пользователь хочет узнать про планету: ' + planet)
    if planet.lower() == 'mars':
        update.message.reply_text('Вы хотите узнать про созвездие планеты ' + planet)
        constellation = ephem.constellation(ephem.Mars(datetime.datetime.now()))
        update.message.reply_text('Планета ' + planet + ' в созвездии ' + constellation[1])
    else:
        update.message.reply_text('Не знаю такой планеты (')

def word_count(bot,update):
    user_words = update.message.text
    update.message.reply_text('Вы написали слова: \n' + user_words)

def talk_to_me(bot, update):
    user_text = update.message.text
    print('Пользователь написал: ' + user_text)
    update.message.reply_text('Ваше обращение будет обработано')

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater(secret_key, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_to_const))
    dp.add_handler(CommandHandler("wordcount", word_count))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

# Вызываем функцию - эта строчка собственно запускает бота
main()
