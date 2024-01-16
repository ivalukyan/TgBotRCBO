"""
Menu
"""

from telebot import types

from notion.nt import create_page
from datetime import (datetime, timezone, date, timedelta)


def startMenu(message: any):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("📆 NOTTION 📒")
    button2 = types.KeyboardButton("🔗 Полезные материалы")
    markup.add(button1, button2)
    return markup


def adminMenu(message: any):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("📝Новая запись")
    button2 = types.KeyboardButton("❌Удалить запись")
    button3 = types.KeyboardButton("✅Получить запись")
    button4 = types.KeyboardButton("🔙")
    markup.add(button1, button2, button3, button4)
    return markup


def urlMenu(message: any):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Английский язык",
                                         url="https://drive.google.com/file/d"
                                                       "/1Da9rzpImPVHXgkp2gt8lmFnGhrhAOHJ-/view?usp=drive_link")
    button2 = types.InlineKeyboardButton(text="Дифференциальные уравнения",
                                         url="https://drive.google.com/file/d/1cKBOjvzZlsV2d6U7pBjnmcsWT"
                                                       "-_9fDNe/view?usp=drive_link")
    button3 = types.InlineKeyboardButton(text="Математический анализ",
                                         url="https://drive.google.com/file/d"
                                                       "/1wMBytaVoDOS5VP5W_I8XxFeVCQxrZ9ra/view?usp=drive_link")
    button4 = types.InlineKeyboardButton(text="Прикладная механика",
                                         url="https://drive.google.com/file/d"
                                                       "/1m8SkH6YkVWUEDm1blVxL_rMiIuktTtfC/view?usp=drive_link")
    button5 = types.InlineKeyboardButton(text="Физика Сборник Иродов",
                                         url="https://drive.google.com/file/d"
                                                       "/1m8SkH6YkVWUEDm1blVxL_rMiIuktTtfC/view?usp=drive_link")
    button6 = types.InlineKeyboardButton(text="Физика сборник Чертов",
                                         url="https://drive.google.com/file/d"
                                                       "/1dQjxdxx_ix92NglQippmX8cjxlZhXNm8/view?usp=drive_link")
    markup.add(button1, button2, button3, button4, button5, button6)
    return markup


def notionMenu(message: any):
    days_of_week = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']

    markup = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton(text=days_of_week[(get_day_of_week() - timedelta(days=3)).weekday()],
                                      callback_data=f"{getTime() - timedelta(days=3)}")
    but2 = types.InlineKeyboardButton(text=days_of_week[(get_day_of_week() - timedelta(days=2)).weekday()],
                                      callback_data=f"{getTime() - timedelta(days=2)}")
    but3 = types.InlineKeyboardButton(text=days_of_week[(get_day_of_week() - timedelta(days=1)).weekday()],
                                      callback_data=f"{getTime() - timedelta(days=1)}")
    but4 = types.InlineKeyboardButton(text=days_of_week[get_day_of_week().weekday()], callback_data=f"{getTime()}")
    but5 = types.InlineKeyboardButton(text=days_of_week[(get_day_of_week() + timedelta(days=1)).weekday()],
                                      callback_data=f"{getTime() + timedelta(days=1)}")
    but6 = types.InlineKeyboardButton(text=days_of_week[(get_day_of_week() + timedelta(days=2)).weekday()],
                                      callback_data=f"{getTime() + timedelta(days=2)}")
    but7 = types.InlineKeyboardButton(text=days_of_week[(get_day_of_week() + timedelta(days=3)).weekday()],
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


def get_day_of_week():
    return datetime.now()


def getTime():
    _today = date.today()
    return _today


def get_text(sub_arr, task_arr, tag_arr, status_arr, i) -> str:
    return (f"===================\n📚<b><i>ПРЕДМЕТ:</i></b> {sub_arr[i]}\n---------------------------\n"
            f"✏️<b><i>ИНФО:</i></b>\n{task_arr[i]}\n---------------------------"
            f"\n<b><i>ТИП:</i></b> {tag_arr[i]}\n---------------------------\n"
            f"<b><i>СТАТУС:</i></b> {status_arr[i]}\n===================\n\n\n")
