# recursion is  nothing but a function calling itself
""""
let's take an example of factorial of a number
factorial(0)=1
factorial(1)=1
factorial(2)=1 x 2
factorial(3)=1 x 2 x 3
factorial(4)=1 x 2 x 3 x 4
factorial(5)=1 x 2 x 3 x 4 x 5
factorial(n)= n x factorial(n-1)  # this is called recursive case
"""
def factorial(n):
    fact=n*factorial(n-1) if n>1 else 1
    return fact
n=int(input("Enter  a number you want factorial of: "))
a=factorial(n)
print(f"The factorial of {n} is {a}")