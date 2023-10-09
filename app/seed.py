import os
command = os.system
from config.tenants.db_list import DB_LIST

def migrate_all_db():
    command("python3 app/manage.py makemigrations")
    for i in DB_LIST:
        cmd = f"python3 app/manage.py migrate --database={i['key']}"
        print(f"Migrate For {i['key']}")
        command(cmd)


if __name__ == '__main__':
    migrate_all_db()
    # command("python app/manage.py runserver")