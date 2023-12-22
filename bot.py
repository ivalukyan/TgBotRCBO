"""
Bot
"""
import telebot

from auth.auth import auth_message
from env import TOKEN

from env import TO_CHAT_ID

from menu import startMenu, urlMenu, notionMenu

from notion.nt import create_page, get_pages
from datetime import (datetime, timezone, date, timedelta)

# Token
token = TOKEN

# Initialized bot
rcbo = telebot.TeleBot(TOKEN)


# Commands (CRUD)
@rcbo.message_handler(commands=['start'])
def create_rcbo(message: any):
    """
    Function for create dialog
    """
    if auth_message(message) != 1:
        rcbo.send_message(message.chat.id, f"Hi, {message.from_user.first_name}", reply_markup=startMenu(message))
    else:
        rcbo.send_message(message.chat.id, f"Hi, {message.from_user.first_name}", reply_markup=startMenu(message))


@rcbo.message_handler(commands=['update'])
def user_id(message: any):
    if message == '/update' and auth_message(message) == 1:
        msg = rcbo.send_message(message.chat.id, "Enter your phone ---> ")
        rcbo.register_next_step_handler(msg, update_rcbo)


def update_rcbo(message: any):
    """
    Function for update dialog
    """
    if auth_message(message) != 1:
        phone = ""


@rcbo.message_handler(content_types=["text"])
def answer(message: any):
    if auth_message(message) == 1 and message.text.lower() == "create task":

        msg = rcbo.send_message(message.chat.id, "Enter DATA --> \nExample => \n\nPhysics\ntask 378")

    elif auth_message(message) == 1 and message.text.lower() == "get info":
        rcbo.send_message(message.chat.id, "INFO FROM DATABASE")

    elif message.text == "📆 NOTTION 📒":
        rcbo.send_message(message.chat.id, "Выберите день: ", reply_markup=notionMenu(message))

    elif message.text == "🔗 Полезные материалы":
        rcbo.send_message(message.chat.id, "Выберите файл: ", reply_markup=urlMenu(message))


def recent_message(message: any):
    rcbo.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)


@rcbo.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    usl = call.data

    pages = get_pages()
    for page in pages:
        props = page["properties"]
        sub = props["Subjects"]["title"][0]["text"]["content"]
        #task = props["Tasks"]["rich_text"][0]["text"]["content"]
        tag = props["Tags"]["multi_select"][0]["name"]
        #tag_1 = props["Tags"]["multi_select"][1]["name"]
        publish = props["Published"]["date"]["start"]
        published = datetime.fromisoformat(publish).date()

        if f"{published}" == f"{usl}":
            rcbo.send_message(call.message.chat.id, f"===================\n"
                                                    f"📚Предмет: {sub}\n------------------------------\n"
                                                    f"✏️Задание: task\n------------------------------\n"
                                                    f"🔵Тип: {tag}\n"
                                                    f"\n===================\n")


# Start bot
if __name__ == "__main__":
    rcbo.polling()
