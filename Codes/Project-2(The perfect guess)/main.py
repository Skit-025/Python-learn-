from random import randint as rni
Comupter_guess=rni(1,100)

l=[]

# print(Comupter_guess)# Test print

User_guess=int(input("Enter a number in between 1 to 100: "))

l.append(User_guess)

# print(User_guess) Test print

while(Comupter_guess!=User_guess):
    if Comupter_guess>User_guess:
        print("Try a larger number")
        User_guess=int(input("Enter again:"))
        l.append(User_guess)
        
    else:
        print("Try a smaller number")
        User_guess=int(input("Enter again:"))
        l.append(User_guess)

else:
    a=len(l)
    print(f"Yeah you found the {User_guess} in attempt {a}\n")
    print("Next Player can join now\n")

Comupter_guess=rni(1,100)
User_guess=int(input("Enter a number in between 1 to 100: "))
L=[]
while(Comupter_guess!=User_guess):
    if Comupter_guess>User_guess:
        print("Try a larger number")
        User_guess=int(input("Enter again:"))
        L.append(User_guess)
        
    else:
        print("Try a smaller number")
        User_guess=int(input("Enter again:"))
        L.append(User_guess)

else:
    b=len(L)
    print(f"Yeah you found the {User_guess} in attempt {b}")
    if a<b:
        print("Player1 own")
    else:
        print("Player2 won")