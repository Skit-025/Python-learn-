import random as ra
def game(name):
    score=ra.choice(range(1,101))
    return score ,name
a=game(name=input("Enter your name: "))
print(a)# for testing
high_score=0,None
with open("Score_store.txt","a+") as f:
    f.seek(0)
    scores=f.readlines()
    if scores==[]:
        f.write(f"{a[0]},{a[1]}\n")
        high_score=a
        print(f"Congratulations {a[1]}! You have the highest score of {a[0]}.")
    else:
        f.seek(0)
        parsed=[line.strip().split(",") for line in scores]
        parsed=[(int(s[0]), s[1]) for s in parsed]
        high_score=max(parsed, key=lambda x: x[0])
        if a[0]>high_score[0]:
            f.write(f"{a[0]},{a[1]}\n")
            high_score=a
            print(f"Congratulations {a[1]}! You have the highest score of {a[0]}.")
        else:
            print(f"Sorry {a[1]}, your score of {a[0]} did not beat the highest score of {high_score[0]} held by {high_score[1]}. Better luck next time!")


