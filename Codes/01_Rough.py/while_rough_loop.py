n=int(input("enter any number :"))
i=2
count=0
if n>1:
    while(i<n):
        if n%i==0:
            count+=1
        i+=1
    if count==1:
        print("You found a composite number!!,Retry let's see what else you gonna grab")
    else:
        print("Entered number is prime,please retry may be you will find a composite one!!")
else:
    print("please enter a number values more than one(1)")