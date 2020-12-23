import sqlite3
from florida_scrape import florida_results

#days_month = [['01', '31'], ['02', '29'], ['03', '31'], ['04', '30'], 
#            ['05', '31'], ['06', '30'], ['07', '31'], ['08', '31'], 
#            ['09', '30'], ['10', '31'], ['11', '30'], ['12', '31']]

month = '03'
day = '05'

# Get results
results = florida_results(month, day)
print('Results to add: ' + str(len(results)))

# Connect to database
conn = sqlite3.connect('database.db')

# Create a cursor
c = conn.cursor()

# Add reuslts from scrape
#TODO: Work on implementing adding results in the SQL Database

for i in range(len(results)):
    c.executemany("INSERT INTO headlines VALUES ('datecode', 'title', 'link')", (results))
    conn.commit()
    
print('Command exected sucessfully for ' + str(month) + ' ' + str(day))

# Close our connection
conn.close()