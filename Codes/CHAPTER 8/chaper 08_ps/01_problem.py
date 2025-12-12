def grt(a,b,c):
    if a>b>c:
        return a
    elif(b>c>a):
        return b
    elif(c>b>a):
        return c
print("The greatest number :",grt(a=int(input("Enter number")),b=int(input("Enter number")),c=int(input("Enter number"))))
