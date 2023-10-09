from pathlib import Path
# from ...db_list import DB_LIST
from .db_list import DB_LIST
BASE_DIR = Path(__file__).resolve().parent.parent

def get_database():
    data = {}
    for i in DB_LIST:
        data[i['key']] = {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / f'{i["db_name"]}.sqlite3'
        }
    return data


DATABASES = get_database()