import telebot
from telebot import types
from const import TOKEN

# Token
token = TOKEN

# Initialized bot
rcbo = telebot.TeleBot(TOKEN)

# Comands (CRUD)
@rcbo.message_handler(commands=['start'])
def create_rcbo(message):
    """
    Function for create dialog
    """
    pass

@rcbo.message_handler(commands=['update'])
def update_rcbo(message):
    """
    Function for update dialog
    """
    pass

@rcbo.message_handler(commands=['delete'])
def delete_rcbo(message):
    """
    Function for delete dialog
    """


# Start bot
rcbo.polling()