from telebot import types

def phone_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Поделиться номером',
                                  request_contact=True)
    kb.add(button)
    return kb
def location_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Поделиться локацией',
                                  request_location=True)
    kb.add(button)
    return kb