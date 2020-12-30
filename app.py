from cs50 import SQL
from flask import Flask, flash, redirect, url_for, render_template, request
import sqlite3
from florida_scrape import florida_results
from datetime import date
import random

# Create connection to flask
app = Flask(__name__)

@app.route("/")
def home():
    return redirect("/today")

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
    if len(datecode) == 4:
        # Test captured month and day
        # datecode_len = len(datecode)
        month = datecode[:2]
        day = datecode[2:]

        # Establish connection to SQL database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
            
        sql_day = day.lstrip('0') # Strip out leading zero from day
        sql_date = str(month) + str(sql_day)
        
        querys = c.execute("SELECT title, url FROM headlines WHERE datecode = ?", (sql_date,))

        return render_template("anydate.html", month = month, day = day, querys = querys)
    else:
        return render_template("today.html")

@app.route("/birthday", methods = ["GET", "POST"])
def birthday():
    if request.method == "POST":
        if not request.form.get("birthday"):
        # TODO: Sometime button doesn't return with any information
            # flash("Please provide birthday")
            return render_template("today.html")
        else:
            birthday_input = request.form.get("birthday") # Capture inputted DOB '2020-12-28'
            birthday_split = birthday_input.split('-')  # Split DOB into list of year, month, day
            if len(birthday_split) == 3:    # If month
                day = birthday_split[2]
                month = birthday_split[1]

                # Establish connection to SQL database
                conn = sqlite3.connect('database.db')
                c = conn.cursor()

                # Search database for results
                sql_day = day.lstrip('0') # Strip out leading zero from day
                sql_date = str(month) + str(sql_day)
        
                querys = c.execute("SELECT title, url FROM headlines WHERE datecode = ?", (sql_date,))

                # flash("Success!")
                return render_template("birthday.html", month = month, day = day, querys = querys)
            else:
                return render_template("today.html", dob = birthday_split)
    else:
        return render_template("today.html")


@app.route("/archive", methods = ["GET", "POST"])
def archive():
    return render_template("archive.html")

# TODO:
    # Search date within the search bar
    # Setup archvie page to access any date of the year (show )
    # Word cloud???



if __name__ == "__main__":
    app.run(debug=True)