import csv

def find_total_visits(file_names):
    total_visits = 0
    for file in file_names:
        try:
            with open(file, 'r') as FILE:
                csv_reader = csv.DictReader(FILE)
                for row in csv_reader:
                    try:
                        visits = int(row['Alice', 'Bob', 'Charlie'])
                        total_visits += visits
                    except ValueError:
                        print(f"Error in {file}: Invalid data in the row {row}.")
        except FileNotFoundError:
            print(f"Error: File '{file}' not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def ex2():
    total = find_total_visits(["week-1.csv", "week-2.csv", "week-3.csv"])
    print(f"Total visits: {total}.")

ex2()