"""
Menu
"""

from telebot import types

from notion.nt import create_page, get_pages
from datetime import (datetime, timezone, date, timedelta)


def startMenu(message: any):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("📆 NOTTION 📒")
    button2 = types.KeyboardButton("🔗 Полезные материалы")
    markup.add(button1, button2)
    return markup


def urlMenu(message: any):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Английский язык",
                                         url="https://drive.google.com/file/d/1Da9rzpImPVHXgkp2gt8lmFnGhrhAOHJ-/view?usp=drive_link")
    button2 = types.InlineKeyboardButton(text="Дифференциальные уравнения",
                                         url="https://drive.google.com/file/d/1cKBOjvzZlsV2d6U7pBjnmcsWT-_9fDNe/view?usp=drive_link")
    button3 = types.InlineKeyboardButton(text="Математический анализ",
                                         url="https://drive.google.com/file/d/16WrWFoLw-sIiMW_0AkCDDxT0HUabWZ7Z/view?usp=drive_link")
    button4 = types.InlineKeyboardButton(text="Прикладная механика",
                                         url="https://drive.google.com/file/d/1wMBytaVoDOS5VP5W_I8XxFeVCQxrZ9ra/view?usp=drive_link")
    button5 = types.InlineKeyboardButton(text="Физика Сборник Иродов",
                                         url="https://drive.google.com/file/d/1m8SkH6YkVWUEDm1blVxL_rMiIuktTtfC/view?usp=drive_link")
    button6 = types.InlineKeyboardButton(text="Физика сборник Чертов",
                                         url="https://drive.google.com/file/d/1dQjxdxx_ix92NglQippmX8cjxlZhXNm8/view?usp=drive_link")
    markup.add(button1, button2, button3, button4, button5, button6)
    return markup


def notionMenu(message: any):
    markup = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton(text=(getTime() - timedelta(days=3)).strftime("%d-%m-%Y"),
                                      callback_data=f"{getTime() - timedelta(days=3)}")
    but2 = types.InlineKeyboardButton(text=(getTime() - timedelta(days=2)).strftime("%d-%m-%Y"),
                                      callback_data=f"{getTime() - timedelta(days=2)}")
    but3 = types.InlineKeyboardButton(text=(getTime() - timedelta(days=1)).strftime("%d-%m-%Y"),
                                      callback_data=f"{getTime() - timedelta(days=1)}")
    but4 = types.InlineKeyboardButton(text=getTime().strftime("%d-%m-%Y"), callback_data=f"{getTime()}")
    but5 = types.InlineKeyboardButton(text=(getTime() + timedelta(days=1)).strftime("%d-%m-%Y"),
                                      callback_data=f"{getTime() + timedelta(days=1)}")
    but6 = types.InlineKeyboardButton(text=(getTime() + timedelta(days=2)).strftime("%d-%m-%Y"),
                                      callback_data=f"{getTime() + timedelta(days=2)}")
    but7 = types.InlineKeyboardButton(text=(getTime() + timedelta(days=3)).strftime("%d-%m-%Y"),
                                      callback_data=f"{getTime() + timedelta(days=3)}")
    markup.add(but1, but2, but3, but4, but5, but6, but7)
    return markup


# Create new task
def data(message: any):
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


def getTime():
    _today = date.today()
    return _today
