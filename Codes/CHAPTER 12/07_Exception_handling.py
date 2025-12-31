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