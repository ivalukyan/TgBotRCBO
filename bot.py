"""
Bot
"""
import telebot

from auth.auth import auth_message
from env import TOKEN

from dbschemas.user import create_table, update_table, delete_person

from notion.nt import create_page

from datetime import datetime,timezone


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
    if auth_message(message) != 1:
        create_table(message)


@rcbo.message_handler(commands=['update'])
def user_id(message):
    if message == '/update' and auth_message(message) == 1:
        msg = rcbo.send_message(message.chat.id, "Enter your phone ---> ")
        rcbo.register_next_step_handler(msg, update_rcbo)


def update_rcbo(message):
    """
    Function for update dialog
    """
    if auth_message(message) != 1:
        phone = ""
        update_table(message, phone)


@rcbo.message_handler(commands=['delete'])
def user_id(message):
    if message == '/delete' and auth_message(message) == 1:
        msg = rcbo.send_message(message.chat.id, "Enter ID person ---> ")
        rcbo.register_next_step_handler(msg, delete_rcbo)


def delete_rcbo(message):
    """
    Function for delete dialog
    """
    if auth_message(message) == 1:
        UserId = message.text
        delete_person(UserId)


@rcbo.message_handler(content_types=["text"])
def answer(message):
    if auth_message(message) == 1 and message.lower() == "create task":

        msg = rcbo.send_message(message.chat.id, "Enter DATA --> \nExample => \n\nPhysics\ntask 378")
        rcbo.register_next_step_handler(msg, data)


def data(message):
    _data = message.text.split("\n")
    print(_data)

    subject = _data[0]
    task = _data[1]
    published_date = datetime.now().astimezone(timezone.utc).isoformat()

    data = {
        "Subjects": {"title": [{"text": {"content": subject}}]},
        "Tasks": {"rich_text": [{"text": {"content": task}}]},
        "Published": {"date": {"start": published_date, "end": None}}
    }
    create_page(data)


# Start bot
if __name__ == "__main__":
    rcbo.polling()
