import sqlite3
from flask import request

def database_query(month, day):
    # Make connection to database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Make query to database
    sql_day = day.lstrip('0') # Strip out leading zero from day
    sql_date = str(month) + str(sql_day)
    querys = c.execute("SELECT title, url FROM headlines WHERE datecode = ?", (sql_date,))
    return querys

def detect():
    browser = request.user_agent.browser
    platform = request.user_agent.platform

    if browser and platform:
        if (platform == 'macos' or platform == 'windows' and browser == 'safari'):
            return True
        else:
            return False

    