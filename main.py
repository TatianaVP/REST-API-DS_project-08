import telebot
import requests
import buttons as b

bot = telebot.TeleBot('5601376239:AAGhNX8afEOC9AHZJFSmEHwBQfmXa3ucwnM')


class CurrencyApi:
    def __init__(self):
        self.url = 'https://cdn.cur.su/api/cbr.json'

    def get_currencies(self):
        response = requests.get(self.url)
        response_dict = response.json()
        usd_rub = round(response_dict['rates']['RUB'] / response_dict['rates']['USD'], 2)
        eur_rub = round(response_dict['rates']['RUB'] / response_dict['rates']['EUR'], 2)
        return f'1 евро = {eur_rub} рублей\n 1 доллар США = {usd_rub} рублей'

    def convert_currencies(self, quan, cur1, cur2):
        response = requests.get(self.url)
        response_dict = response.json()
        quan = int(quan)
        result = round(quan * response_dict['rates'][cur2] / response_dict['rates'][cur1], 2)
        return f'{quan} {cur1} = {result} {cur2}'


currency = CurrencyApi()


@bot.message_handler(commands=['start'])
def start_message(message):
    msg = bot.send_message(message.chat.id, 'Привет, выберите категорию:', reply_markup=b.source_markup)
    bot.register_next_step_handler(msg, ask_category)


def ask_category(message):
    if message.text == 'Курс':
        bot.send_message(message.chat.id, currency.get_currencies(), reply_markup=b.start_markup)

    elif message.text == 'Конвертер':
        msg = bot.send_message(message.chat.id, 'Выберите базовую валюту:', reply_markup=b.currency_markup)
        bot.register_next_step_handler(msg, ask_currency_base)


def ask_currency_base(message):
    base_currency = message.text
    msg = bot.send_message(message.chat.id, 'Выберите количество: ')
    bot.register_next_step_handler(msg, ask_quantity, base_currency)


def ask_quantity(message, base_curr):
    quant = message.text

    if not quant.isdigit():
        msg = bot.send_message(message.chat.id, 'Количество должно быть числом. Повторите')
        bot.register_next_step_handler(msg, ask_quantity)
        return
    msg = bot.send_message(message.chat.id, 'Выберите вторую валюту:', reply_markup=b.currency_markup)
    bot.register_next_step_handler(msg, ask_currency_second, base_curr, quant)


def ask_currency_second(message, base_currency, quantity):
    second_currency = message.text
    bot.send_message(message.chat.id, currency.convert_currencies(quantity, base_currency, second_currency),
                     reply_markup=b.start_markup)


bot.infinity_polling()
