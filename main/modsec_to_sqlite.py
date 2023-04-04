import re
import sqlite3

# Open the log file for reading
with open('modsec.log', 'r') as f:

    # Compile a regular expression to extract the relevant data
    regex = re.compile(r'\[(?P<date>[^]]+)\] (?P<client_ip>\d+\.\d+\.\d+\.\d+) (?P<server_ip>\d+\.\d+\.\d+\.\d+) \d+ \d+ \[(?P<rule_id>\d+):(?P<msg_id>[^\]]+)\] .*')

    # Open the SQLite database for writing
    conn = sqlite3.connect('modsec.db')
    c = conn.cursor()

    # Create the table for storing the data
    c.execute('''CREATE TABLE IF NOT EXISTS modsec_logs
                 (date TEXT, client_ip TEXT, server_ip TEXT, rule_id TEXT, msg_id TEXT)''')

    # Read the log file line by line
    for line in f:
        # Try to match the regular expression against the line
        match = regex.match(line)
        if match:
            # Extract the relevant data from the match object
            date = match.group('Date')
            client_ip = match.group('Host')
            server_ip = match.group('Server')
            rule_id = match.group('ModSecurity')
            msg_id = match.group('msg_id')

            # Insert the data into the database
            c.execute("INSERT INTO modsec_logs VALUES (?, ?, ?, ?, ?)", (date, client_ip, server_ip, rule_id, msg_id))

    # Commit the changes to the database and close the connection
    conn.commit()
    conn.close()


# Here's how you can use this script:

# Save the above code into a file named modsec_to_sqlite.py.
# Place the ModSecurity log file that you want to read into the same directory as the Python script, and name it modsec.log.
# Open a command prompt or terminal window, and navigate to the directory containing the Python script and the log file.
# Run the Python script by typing python modsec_to_sqlite.py and pressing Enter.
# The script will read the log file, extract the relevant data using a regular expression, and save it into an SQLite database named modsec.db. You can then use any SQLite client to query the data in the database.
