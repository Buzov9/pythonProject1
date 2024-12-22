import requests
import telebot
from telegram.ext import CommandHandler

bot = telebot.TeleBot('7759754578:AAHgeVXP3zhIOxjgJZ9uL6Yygjm7vHdS80E')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     'Привет!\n Я бот, который покажет погоду в любой точке мира ☀️🌧️❄️\nПросто напиши нужную локацию/город на английском языке и я отправлю тебе данные.\nНапример: /city London',
                     parse_mode='html')


babah = ['Нагасаки', 'Хиросима', 'Nagasaki', 'Hirosima']


@bot.message_handler(commands=['city'])
def city(message):
    try:
        user_city = message.text.split()[1]
        if user_city in babah:
            temperature = +7712
            bot.send_message(message.chat.id, f"Температура: {temperature} °C")
        else:
            api_key = "80ff8268463421fbb03555f79b67815e"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={api_key}&units=metric"
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                temperature = data['main']['temp']
                bot.send_message(message.chat.id, f"Температура: {temperature} °C")
            else:
                bot.send_message(message.chat.id, "Ошибка при получении данных")
    except:
        bot.send_message(message.chat.id, "Чёртов идиот🤬🤬🤬, введи как в примере!!!\n /citi Moscow")


bot.polling(none_stop=True)
