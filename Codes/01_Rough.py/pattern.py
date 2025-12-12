"""
***
* *
***
"""
n=int(input("enter any number "))
#for n = 3 the above pattern will be printed
for i in range(1,n+1):
    if i==1 or i==n:
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*") 