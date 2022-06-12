from flask import Flask, flash, redirect, url_for, render_template, request, get_flashed_messages
import sqlite3
from functions.florida_scrape import florida_results
from datetime import date
from datetime import datetime
from pytz import timezone
import pytz
import random
from helpers import database_query, detect
from dotenv import load_dotenv
import os


# Create connection to flask
app = Flask(__name__)

# Setup session key
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

@app.route("/")
def home():
    return redirect("/today")

#Return horoscope for today's date'''
@app.route("/today", methods = ["GET", "POST"])
def today():

    # Calculate today's date adjusted for PST
    date_format='%m-%d'
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('US/Pacific'))
    month_day = date.strftime(date_format).split('-')
    month = str(month_day[0])
    day = month_day[1]

    # Query database
    querys = database_query(month, day)
    
    return render_template("today.html", month = month, day = day, querys = querys)

# Return horoscope for a Random day
@app.route("/random", methods = ["GET", "POST"])
def random_result():

    # Determine valid random month and day

    # Intialize random seed
    seed = random.randint(1, 1000)
    random.seed(seed)

    # Determine random day
    start_date = date.today().replace(day=1, month=1).toordinal()
    end_date = date.today().replace(day=31, month=12).toordinal()
    random_day = date.fromordinal(random.randint(start_date, end_date))
    
    split_date = str(random_day).split('-')
    month = split_date[1]
    day = split_date[2]

    # Query database
    querys = database_query(month, day)

    return render_template("random.html", month = month, day = day, querys = querys)

# Return horoscope for specified day
@app.route("/<string:datecode>")
def anydate(datecode):
    if len(datecode) == 4:
        # Test captured month and day
        # datecode_len = len(datecode)
        month = datecode[:2]
        day = datecode[2:]
    
        # Check date doesn't exceed max calendar day for that month
        max_day = {'01': '31', '02': '29', '03': '31', '04': '30', '05': '31', '06': '30',
        '07' : '31', '08': '31', '09': '30', '10': '31', '11': '30', '12' : '31'}

        if max_day[month] >= day:
            # Query database
            querys = database_query(month, day)
            flash("Date valid", "success")
            return render_template("anydate.html", month = month, day = day, querys = querys)
        else:
            flash("Date cannot exceed days in month", 'error')
            return redirect("/today")
    else:
        flash('Date invalid, must input /MMDD', 'error')
        return redirect("/today")

# Second verison of birthday with revamped navbar form
@app.route("/birthday", methods = ["GET", "POST"])
def birthday():
    if request.method == "POST":
        # If request is empty, return to today
        if request.form.get("navBarSearch") == "":
            return redirect("today.html")
        else:
            formStringMonth = request.form.get("month")
            formday = request.form.get("day")
            # Convert month from string to int
            monthSwitch = {"January": "01", "February": "02", "March": "03", "April" : "04", 
            "May" : "05", "June" : "06", "July" : "07", "August" : "08", 
            "September" : "09", "October" : "10", "November" : "11", "December" : "12"}
            month = monthSwitch[formStringMonth]
            # Add leading zero to day if day is <10
            if (int(formday) < 10):
                day = "0" + str(formday)
            else:
                day = formday
            # Query database
            querys = database_query(month, day)
            flash('Success!', 'success')
            return render_template("birthday.html", month = month, day = day, querys = querys)
    else:
        flash('Use form to sumbit date', 'error')
        return redirect("/today")

        
# Possible Stats Page, not developed yet

# @app.route("/stats", methods = ["GET", "POST"])
# def stats():
#     # Make connection to database
#     conn = sqlite3.connect('database.db')
#     c = conn.cursor()

#     num_entries = c.execute("SELECT COUNT(*) FROM headlines;")

#     return render_template("stats.html", entries = num_entries)

# Testing route for bootstrap/css resdesign

# @app.route("/testcss", methods = ["Get", "POST"])
# def testcss():
#     return render_template("testcss.html")


# About page for the project
@app.route("/about", methods = ["GET", "POST"])
def about():
    return render_template("about.html")
    
# TODO:
    # Setup archvie page to access any date of the year (show )
    # Word cloud???
    # Send Tweet to twitter account
    # Detect Safari webpage, show hint for how to input dates


if __name__ == "__main__":
    app.run(debug=True)