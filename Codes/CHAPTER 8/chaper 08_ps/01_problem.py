# def grt(a,b,c):
#     if a>b>c:
#         return a
#     elif(b>c>a):
#         return b
#     elif(c>b>a):
#         return c
# print("The greatest number :",grt(a=int(input("Enter number")),b=int(input("Enter number")),c=int(input("Enter number"))))
num=int(input("Enter how many numnbers you want to  compare: "))
def greatest():
    l=[]
    for i in range(num):
        a=int(input("Enter number: "))
        l.append(a)
    return max(l)
print("The greatest number is :",greatest())