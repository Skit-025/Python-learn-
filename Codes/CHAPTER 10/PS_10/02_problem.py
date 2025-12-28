class Calculator:
    def __init__(self):
        print("Calculator initialized!")
        return
    def calculator(self,n1,n2=None):
        operation=input("Enter operation (sum, sub, mul, div, square, cube, sqrt, cubrt): ")
        if operation=="sum":
            return print(f"Sum of {n1} and {n2} is :{n1+n2})")
        elif operation=="sub":
            return print(f"Subtraction of {n1} and {n2} is :{n1-n2})")
        elif operation=="mul":
            return print(f"Multiplication of {n1} and {n2} is :{n1*n2})")
        elif operation=="div":
            return print(f"Division of {n1} and {n2} is :{n1/n2})")
        elif operation=="square":
            return print(f"Square of {n1} is :{n1**2})")
        elif operation=="cube":
            return print(f"Cube of {n1} is :{n1**3})")
        elif operation=="sqrt":
            return n1**0.5
        elif operation=="cubrt":
            return print(f"Cube root of {n1} is :{n1**(1/3)})")
        else:
            return "something went wrong, please try again!"
calc=Calculator()
n1=float(input("Enter first number: "))
op=input("Is it a binary operation? (yes/no): ")
if op.lower()=="yes":
    n2=float(input("Enter second number: "))
    calc.calculator(n1,n2)
else:
    calc.calculator(n1)