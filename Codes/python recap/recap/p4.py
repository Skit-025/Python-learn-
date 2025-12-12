n=int(input("Enter a number: \n"))
count=0
for i in range(1,2001):
    temp=n%i
    if(temp==0):
        count+=1
if(count==2):
    print(f"{n} is a prime number")
elif(n==0):
    print(f"{n} you are dealing with a special digit")
elif(n<0):
    print(f"{n} you are dealing with a negative digit")
else:
    print(f"{n} is a composite number")