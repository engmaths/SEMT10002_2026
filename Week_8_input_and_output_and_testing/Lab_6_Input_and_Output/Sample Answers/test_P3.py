# Test script for comparison assignment
#
# run: python test_P3.py ExerciseP3.py
#
# The test script will run your file and check the statements for inconsistency
#
# Note there are security issues with code like this!  Calling user-supplied code from your
# own is not recommended.  This is just a workaround to make it easy to assess.


import subprocess
import csv
import os
import re
import sys

# Path to your robot log program (adjust if needed)
PROGRAM = sys.argv[1] #"ExerciseP3.py"   # your main script filename
LOG_FILE = "log_file.csv"         # the file your program should create

def run_test():

    # Check number of arguments is correct
    if len(sys.argv)!=2:
        print('Incorrect number of arguments entered')
        print('Usage: python', argv[0], '<file to test>')
        raise ValueError('Script name not provided')

    # Run the robot program and capture output
    print("Running", PROGRAM, "...")
    result = subprocess.run(
        [sys.executable, PROGRAM],
        capture_output=True,
        text=True
    )

    # Check that it ran successfully, print some information if there's an error
    if result.returncode != 0:
        print("Program exited with an error:")
        print(result.stderr)
        sys.exit(1)

    # Check that log file exists
    if not os.path.exists(LOG_FILE):
        print("Log file 'log_file.csv' does not exist.")
        sys.exit(1)
    print("Log file 'log_file.csv' created.")

    # Read the log file
    with open(LOG_FILE, newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        print("Log file is empty.")
        sys.exit(1)

    header = rows[0]
    expected_header = ["Time (s)", "Position [x,y]", "Orientation (rads)", "State information"]
    if header != expected_header:
        print("Header row is incorrect.")
        print("Expected:", expected_header)
        print("Found   :", header)
        sys.exit(1)
    print("Header row is correct.")

    data_rows = rows[1:]
    if not data_rows:
        print("No data rows found after header.")
        sys.exit(1)
    print("Found", len(data_rows), "data rows.")

    for i, row in enumerate(data_rows, start=2):
        if len(row) != 4:
            print("Row", i, "does not have 4 columns:", row)
            sys.exit(1)

        timestamp_str, position_str, orientation_str, state = row

        # Check timestamp is numeric and to 3 decimal places
        try:
            timestamp = float(timestamp_str)
            decimals = abs(timestamp * 1000 - round(timestamp * 1000))
            if decimals > 1e-6:
                print("Timestamp not to 3dp in row", i, ":", timestamp)
                sys.exit(1)
        except:
            print("Invalid timestamp in row", i, ":", timestamp_str)
            sys.exit(1)

        # Check position format "[x,y]" and 3 decimal places
        if not ("[" in position_str and "]" in position_str):
            print("Invalid position format in row", i, ":", position_str)
            sys.exit(1)

        try:
            pos_values = position_str.strip('[]').split(',')
            if len(pos_values) != 2:
                raise ValueError
            x, y = [float(v) for v in pos_values]
            for v in [x, y]:
                decimals = abs(v * 1000 - round(v * 1000))
                if decimals > 1e-6:
                    print("Value in position not to 3dp in row", i, ":", v)
                    sys.exit(1)
        except:
            print("Error parsing position in row", i, ":", position_str)
            sys.exit(1)

        # Check orientation is numeric and 3 decimal places
        try:
            orientation = float(orientation_str)
            decimals = abs(orientation * 1000 - round(orientation * 1000))
            if decimals > 1e-6:
                print("Orientation not to 3dp in row", i, ":", orientation)
                sys.exit(1)
        except:
            print("Invalid orientation in row", i, ":", orientation_str)
            sys.exit(1)

        # Check state field
        if state not in ["", "Collision with wall", "Collision with obstacle"]:
            print("Unexpected state in row", i, ":", state)
            sys.exit(1)

    print("All checks passed successfully!")

if __name__ == "__main__":
    run_test()