import random as rnd
print("Welcome to Rock, Paper, Scissors Game!, Made by Skit025")
Computer=rnd.choice([0,1,-1])
player=input("Enter your choice: ").strip().lower()
dictionary={
'rock':0,
'paper':1,
'scissors':-1
}
comp_dic={
    0:'rock',
    1:'paper',
    -1:'scissors'
}
if player not in dictionary:
    print("Invalid choice, try again!")
    exit()
else:
    Player=dictionary[player]
print(f"Computer chose: {comp_dic[Computer]}") #test for computer choice
print(f"You  chose: {comp_dic[Player]}") #test for player choice
def game():
    if Player==Computer:
        print("It's a tie!")
    else:
        if Computer==0 and Player==-1:
            print("Computer wins!")
        elif Computer==0 and Player==1:
            print("You win!")
        elif Computer==1 and Player==-1:
            print("You win!")
        elif Computer==1 and Player==0:
            print("Computer wins!")
        elif Computer==-1 and Player==0:
            print("You win!")
        elif Computer==-1 and Player==1:
            print("Computer wins!")
        else:
            print("something is fishy")
game()