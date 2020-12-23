from cs50 import SQL
from flask import Flask, redirect, url_for, render_template
import sqlite3
from florida_scrape import florida_results
from datetime import date
import random

# Create connection to flask
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

#Return horoscope for today's date'''
@app.route("/today", methods = ["GET", "POST"])
def today():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Setup query for today's date
    today = date.today()
    month = str(today.month)
    day = today.day 
    sql_day = str(int(day)) # Strip out leading zero from day
    sql_date = str(month) + str(sql_day)
    
    querys = c.execute("SELECT title, url FROM headlines WHERE datecode = ?", (sql_date,))

    return render_template("today.html", month = month, day = day, querys = querys)

# Return horoscope for a Random day
@app.route("/random", methods = ["GET", "POST"])
def random_result():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Determine valid random month and day
    start_date = date.today().replace(day=1, month=1).toordinal()
    end_date = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_date, end_date))
    split_date = str(random_day).split('-')
    month = split_date[1]
    day = split_date[2]
    sql_day = str(int(day)) # Strip out leading zero from day
    sql_date = str(month) + str(sql_day)
    querys = c.execute("SELECT title, url FROM headlines WHERE datecode = ?", (sql_date,))

    return render_template("random.html", month = month, day = day, querys = querys)


# Return horoscope for specified day
@app.route("/<string:datecode>")
def anydate(datecode):
    # Test captured month and day
    datecode_len = len(datecode)
    month = datecode[:2]
    day = datecode[2:]

    # Establish connection to SQL database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    sql_day = str(int(day)) # Strip out leading zero from day
    sql_date = str(month) + str(sql_day)
    
    querys = c.execute("SELECT title, url FROM headlines WHERE datecode = ?", (sql_date,))

    return render_template("anydate.html", month = month, day = day, querys = querys)

@app.route("/archive", methods = ["GET", "POST"])
def archive():
    return render_template("archive.html")

# TODO:
    # Fillable form to serach date
    # Search date within the search bar
    # Setup archvie page to access any date of the year (show )



if __name__ == "__main__":
    app.run(debug=True)