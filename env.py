import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

ADM1 = os.getenv('ADM1')
ADM2 = os.getenv('ADM2')
ADM3 = os.getenv('ADM3')
ADM4 = os.getenv('ADM4')
TO_CHAT_ID = os.getenv('TO_CHAT_ID')

NOTION_TOKEN = os.getenv('NOTION_TOKEN_MY')
NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID_MY')
NOTION_URL = os.getenv('NOTION_URL')

PATH = os.getenv('PATH')
