import sqlite3
from florida_scrape import florida_results

# Get results
results = florida_results('03', '04')

# Connect to database
conn = sqlite3.connect('database.db')

# Create a cursor
c = conn.cursor()

# Add reuslts from scarpe

for i in range(len(results)):
    c.execute("INSERT INTO headlines (datecode, text, url) VALUES (?, ?, ?)", 
    (results[i]['datecode'], results[i]['title'], results[i]['link']))
    
print('Command exected sucessfully')

#Commit our command
conn.commit()

# Close our connection
conn.close()