from telebot import types


start_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
start_markup_btn1 = types.KeyboardButton('/start')
start_markup.add(start_markup_btn1)

source_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
source_markup_btn1 = types.KeyboardButton(text='Курс')
source_markup_btn2 = types.KeyboardButton(text='Конвертер')
source_markup.add(source_markup_btn1, source_markup_btn2)

currency_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
currency_markup_btn1 = types.KeyboardButton(text='USD')
currency_markup_btn2 = types.KeyboardButton(text='EUR')
currency_markup_btn3 = types.KeyboardButton(text='RUB')
currency_markup.add(currency_markup_btn1, currency_markup_btn2, currency_markup_btn3)