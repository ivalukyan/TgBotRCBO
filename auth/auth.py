from const import ADM1, ADM2, ADM3, ADM4
from bot import rcbo
def auth(message):
    """
    Function for authentication
    """

    # Users who have admin status
    admin = [ADM1, ADM2, ADM3, ADM4]

    MsgId  = rcbo.get_chat_member(message.from_user.id)
    if MsgId in admin:
        return True
    else:
        return False