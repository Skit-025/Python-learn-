# n=int(input("Enter any number :"))
# fact=1
# if n>1:
#       for i in range(1,n+1):
#             fact*=i
#       print(fact)
# else:
#       print("1")


#Recursion

def factorial(n):
    if (n==0 or n==1):
        return 1
    return n * factorial(n-1)
n=int(input("Enter number :"))
print(f"Factorial is : {factorial(n)}")

# n=int(input("Enter number :"))
# for i in range(1,n+1):
#     print("*"*i)

def pattern():
    for i in range(1,n+1):
        return print("*")            #in appropriate... to be continued 