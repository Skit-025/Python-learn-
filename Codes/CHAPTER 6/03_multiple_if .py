a=int(input("Enter your age :"))
#if statement 1
if(a%2==0):
    print("your age is even")
else:
    print("Your age is odd")    
#End of if statement 1

#if statement 2
if(a>=18):
    print("you are above the age of consent")
elif(a<=0):
    print("Chal be sahi sahi age daal!!")

elif(a==0):
    print("you are a fool")

else:
    print("You are below the age consent")

print("Program Ended")
#End of if statement 2

#else and elif can't be used independently but if can be
