Name=input("Enter your name please :")
Age=int(input("Please enter your Age :"))

if(Age>=18):
    print("You may go inside..,\t")
    print(f"Welcome sir : {Name}\n")
elif(Age<=0):
    print("Pagal ho kya bhiya achese age dalo na.., Chalo firse run karo program ko.. Commands pata h na?\n")
else:
    print("Sorry kid, You are not permitted to get inside..")
print("Session over")