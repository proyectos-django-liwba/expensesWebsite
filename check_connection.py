import os
import django
from django.db import connections
from django.db.utils import OperationalError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "expensesWebsite.settings")
django.setup()


def check_database_connection():
    db_conn = connections["default"]
    try:
        c = db_conn.cursor()
        c.execute("SELECT 1;")
        print("Database connection is OK")
    except OperationalError:
        print("Database connection failed")


if __name__ == "__main__":
    check_database_connection()
