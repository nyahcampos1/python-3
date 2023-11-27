def validate_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        for line_number, line in enumerate(lines, start = 1):
            parts = line.strip().split(',')
            CarId, Miles = parts[0], parts[1]
            try:
                mileage = int(Miles)
            except ValueError:
                print(f"Error in line {line_number}: Mileage for car '{CarId}' is not a valid integer number.")
                continue
        print("File validation completed. No errors found.")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def ex1():
    try:
        validate_file("input.txt")
    except ValidationException as ve:
        print(ve)

ex1()