from pathlib import Path
# from ...db_list import DB_LIST
from .db_list import DB_LIST
BASE_DIR = Path(__file__).resolve().parent.parent

def get_database(path):
    data = {}
    for i in DB_LIST:
        data[i['key']] = {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': path / f'{i["db_name"]}.sqlite3'
        }
    return data


# DATABASES = get_database()