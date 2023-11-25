"""
Database for users
"""

import sqlite3

from env import PATH


async def create_table(message):
    """
    CREATE TABLE
    """
    # Error Handling
    try:
        # Connecting to Database
        connection = sqlite3.connect(f'{PATH}\\users.db')
        cursor = connection.cursor()

        # Create table
        cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
            id INTENGER PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            phone_number TEXT
        )""")

        # Add
        cursor.execute("SELECT name FROM Users WHERE id > ?", (message.from_user.id,))
        if cursor.fetchone() != message.from_user.first_name:
            cursor.execute("INSERT INTO Users(id, name, phone_number) VALUES(?, ?, ?)", (message.from_user.id, message.from_user.first_name, None))

        # Save
        connection.commit()

        # Close database
        connection.close()

    except sqlite3.Error as e:
        print("Ошибка sqlite: ", e)


async def update_table(message, phone: str):
    """
    UPDATE TABLE
    """
    try:
        connection = sqlite3.connect(f'{PATH}\\users.db')
        cursor = connection.cursor()

        cursor.execute("UPDATE Users SET phone = ? WHERE id = ?", (phone, message.from_user.id))

        connection.commit()
        connection.close()
    except sqlite3.Error as e:
        print("Ошибка sqlite: ", e)


async def delete_person(user_id):
    """
    DELETE PERSON
    """
    try:
        connection = sqlite3.connect(f'{PATH}\\users.db')
        cursor = connection.cursor()

        cursor.execute("DELETE FROM Users WHERE id = ?", (user_id,))
    except sqlite3.Error as e:
        print("Ошибка sqlite: ", e)
