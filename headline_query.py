import sqlite3
import time
from florida_scrape import florida_results

# Test for just month of january
days_month = [['05', '31'], ['06', '30'], ['07', '31'], ['08', '31'], 
            ['09', '30'], ['10', '31'], ['11', '30'], ['12', '31']]

for i in range(len(days_month)):
    month = str(days_month[i][0])
    max_days = int(days_month[i][1])
    for j in range(1, (max_days + 1)):

        month = month
        day = j 
        print('Month: ' + month + ' Day: ' + str(j))

        query = florida_results(month, day)
        time.sleep(.5)

        print('Results for ' + str(month) + '-' + str(day) + ' to add: ' + str(len(query)))

        # Create connection
        conn = sqlite3.connect('database.db')

        # Create cursor
        c = conn.cursor()
        for i in range(len(query)):
            c.execute("INSERT INTO headlines (datecode, title, url) VALUES (?, ?, ?)", 
                        (str(query[i]['datecode']), query[i]['title'], query[i]['link']))

            conn.commit()
        print(conn.total_changes)
        time.sleep(.5)


# Add reuslts from scrape
#TODO: Work on implementing adding results in the SQL Database

# Close our connection
# conn.close()