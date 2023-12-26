"""
Bot
"""
import telebot

from auth.auth import auth_message
from env import TOKEN

from env import TO_CHAT_ID

from menu import startMenu, urlMenu, notionMenu, get_text, adminMenu

from notion.nt import create_page, get_pages, delete_page
from datetime import (datetime, timezone)

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


@rcbo.message_handler(content_types=["text"])
def answer(message: any):
    if auth_message(message) == 1 and message.text == "📝Новая запись":

        msg = rcbo.send_message(message.chat.id, "<b><i>Enter DATA</i></b>\n-->\n\n<i>Example:</i>\n\nPhysics\ntask 378\nОбязательно",
                                parse_mode='HTML')
        rcbo.register_next_step_handler(msg, new_task)

    elif auth_message(message) == 1 and message.text == "❌Удалить запись":
        msg = rcbo.send_message(message.chat.id, "<b>Напишите номер страницы которую вы хотите удалить:</b>",
                                parse_mode='HTML')
        rcbo.register_next_step_handler(msg, del_task)

    elif message.text == "✅Получить запись" and auth_message(message) == 1:
        rcbo.send_message(message.chat.id, "<i>Выберите день: </i>", reply_markup=notionMenu(message),
                          parse_mode='HTML')
    elif message.text == "🔙" and auth_message(message) == 1:
        rcbo.send_message(message.chat.id, "<i>Back home menu</i>", reply_markup=startMenu(message), parse_mode='HTML')

    elif message.text == "📆 NOTTION 📒":
        if auth_message(message) == 1:
            rcbo.send_message(message.chat.id, "<b>Команды для админа!</b>", reply_markup=adminMenu(message),
                              parse_mode='HTML')
        else:
            rcbo.send_message(message.chat.id, "Выберите день: ", reply_markup=notionMenu(message))

    elif message.text == "🔗 Полезные материалы":
        rcbo.send_message(message.chat.id, "Выберите файл: ", reply_markup=urlMenu(message))


def recent_message(message: any):
    rcbo.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)


def new_task(message: any):
    texts = message.text.split("\n")
    task = texts[1]
    subject = texts[0]
    tag = texts[2]
    published_date = datetime.now().astimezone(timezone.utc).isoformat()

    data = {
        "Subjects": {"title": [{"text": {"content": subject}}]},
        "Tasks": {"rich_text": [{"text": {"content": task}}]},
        "Tags": {"multi_select": [{"name": tag}]},
        "Published": {"date": {"start": published_date, "end": None}}
    }
    create_page(data)
    rcbo.send_message(message.chat.id, "<b>Запись создана!</b>", parse_mode='HTML')


def del_task(message: any):
    msg = "{}".format(message.text)
    pageArr = []
    pages = get_pages()
    for page in pages:
        page_id = page[id]
        pageArr.append(page_id)

    delete_page(pageArr[int(msg)])


@rcbo.callback_query_handler(func=lambda call: True)
def callback_handler(call):

    if call.data not in ["Английский язык", "Дифференциальные уравнения",
                         "Математический анализ", "Прикладная механика",
                         "Физика Сборник Иродов", "Физика сборник Чертов"]:

        usl = call.data
        message_text = f"<b>{usl}</b>\n"
        len_arr = 0
        subjects_arr = []
        task_arr = []
        tag_arr = []

        pages = get_pages()
        for page in pages:
            props = page["properties"]
            sub = props["Subjects"]["title"][0]["text"]["content"]
            task = props["Tasks"]["rich_text"][0]["text"]["content"]
            tag = props["Tags"]["multi_select"][0]["name"]
            publish = props["Published"]["date"]["start"]
            published = datetime.fromisoformat(publish).date()

            if f"{published}" == f"{usl}":
                len_arr += 1
                subjects_arr.append(sub)
                task_arr.append(task)
                tag_arr.append(tag)

        if subjects_arr != [] and task_arr != [] and tag_arr != []:
            for i in range(0, len_arr):
                message_text += get_text(subjects_arr, task_arr, tag_arr, i)
        else:
            message_text += "<b><i>На данный день нет информации!</i></b>"

        rcbo.send_message(call.message.chat.id, message_text, parse_mode='HTML')

    else:
        pass


# Start bot
if __name__ == "__main__":
    rcbo.polling()
