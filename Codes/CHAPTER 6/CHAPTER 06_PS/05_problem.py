li=[]
li.append("harish")
li.append("Rama")
li.append("harry")
li.append("Aditya")
Name=input("Hey what's up?...\nPlease enter your name:")
if(Name in li):
    print("Congrats!!!\n \t",f"Your name:{Name}, is in the list")
else:
    print(li)