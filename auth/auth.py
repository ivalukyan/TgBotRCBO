from env import ADM1, ADM2, ADM3, ADM4


def auth_message(message):
    """
    Function for authentication
    """

    # Users who have admin status
    admin = [ADM1, ADM2, ADM3, ADM4]
    msgId = message.chat.id
    if f'{msgId}' in admin:
        return True
    return False
