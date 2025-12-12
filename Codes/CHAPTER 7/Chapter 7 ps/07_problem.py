#  * 
# *** 
#***** question
# for i in range(1,4):
#     print("*"*i)
#     i+=2
i=1
n=3
while(i<=n): 
    star1=("*"*(2*i-1))
    space1=(" "*(n-i))
    print(space1+star1)
    i+=1
n=int(input("Enter the value of n"))
for i in range(1,n+1):
    star=("*"*(2*i-1))
    space=(" "*(n-i))
    print(space+star)