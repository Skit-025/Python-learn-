# * * * 
# *   *    for n = 3 
# * * * 
# n=int(input("Enter the value of n"))    #Foooolish method but correct for n=3
# for i in range(2,n+1):
#     print("*"*n)
#     if i==2:
#         print("*"+" "+"*")

n=int(input("Enter the value of n"))    
for i in range(1,n+1):
    if i==1 or i==n:
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")
        
    