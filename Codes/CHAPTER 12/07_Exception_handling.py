try:
    print("hello")
except Exception as e:
    print(e)

try:
    # Code that may raise exceptions
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    # Handles division by zero
    print("Error: Division by zero is not allowed.")

except TypeError:
    # Handles type mismatch errors
    print("Error: Invalid type used in operation.")

except ValueError:
    # Handles invalid input conversion (like entering text instead of a number)
    print("Error: Please enter valid integers only.")

except Exception as e:
    # Handles all other exceptions
    print("An unexpected error occurred:", e)

"""try with a else clause"""

try:
    print("Hello")
except Exception as e:
    print(e)
else:
    print("Something else")

"""Raise keyword use"""

def name(self, value):
    if not isinstance(value, str):
        raise ValueError("Name must be a string")
    self._name = value

"""Try with Finally"""

def read_file(filename):
    try:
        f = open(filename, "r")
        print("File opened successfully!")
        # Simulate reading
        data = f.read()
        print("File content:", data)
    finally:
        print("Closing file...")
        f.close()

# Example call
read_file("example.txt")