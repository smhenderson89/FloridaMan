import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create cursor
c = conn.cursor()

# Test
c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@codemy.com')")

# Commit our command
conn.commit()

# Close our connection
conn.close()