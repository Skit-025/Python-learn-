L1=[]
num1=float(input("Enter number: \n"))
num2=float(input("Enter number: \n"))
num3=float(input("Enter number: \n"))
num4=float(input("Enter number: \n"))
L1.append(num1)
L1.append(num2)
L1.append(num3)
L1.append(num4)
if(num1 >0 and num2>0 and num3>0 and num4>0 ):
    if(num1 >=num2 and num1 >=num3 and num1>=num4):
        print(f"NUMBER 1 IS THE GREATEST: {num1}")

    if(num2 >=num1 and num2 >=num3 and num2>=num4):
        print(f"NUMBER 2 IS THE GREATEST: {num2}")

    if(num3 >=num1 and num3 >=num2 and num3>=num4):
        print(f"NUMBER 3 IS THE GREATEST: {num3}")

    if(num4 >=num1 and num4 >=num2 and num4>=num3):
        print(f"NUMBER 1 IS THE GREATEST: {num1}")

else:
    print("Correct the numbers")
print(L1)
print("Session ended")
