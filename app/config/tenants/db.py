from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

DB_LIST = [
    {
        "key":"indranil", 
        "db_name":"db1", 
        "domain":"indranil",
    },
    {
        "key":"default", 
        "db_name":"db", 
        "domain":"demo",
    },
]

def get_database():
    data = {}
    for i in DB_LIST:
        data[i['key']] = {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / f'{i["db_name"]}.sqlite3'
        }
    return data


DATABASES = get_database()