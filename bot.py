"""
Bot
"""
import telebot

from auth.auth import auth_message
from telebot import types
from env import TOKEN

from dbschemas.user import create_table

from notion.nt import create_page, get_pages, update_page, delete_page


# Token
token = TOKEN

# Initialized bot
rcbo = telebot.TeleBot(TOKEN)


# Commands (CRUD)
@rcbo.message_handler(commands=['start'])
def create_rcbo(message):
    """
    Function for create dialog
    """

    if auth_message(message) == 1:
        create_table(message)
    else:
        pass


@rcbo.message_handler(commands=['update'])
def update_rcbo(message):
    """
    Function for update dialog
    """

    if auth_message(message) == 1:
        pass
    else:
        pass


@rcbo.message_handler(commands=['delete'])
def delete_rcbo(message):
    """
    Function for delete dialog
    """

    if auth_message(message) == 1:
        pass
    else:
        pass


@rcbo.message_handler(content_types=["text"])
def answer(message):
    rcbo.send_message(message.chat.id, "Hi")


# Start bot
if __name__ == "__main__":
    rcbo.polling()
