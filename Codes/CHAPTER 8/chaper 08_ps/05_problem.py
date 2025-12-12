def pattern(n):
    for i in range((n+1),0,-1):
        print("*"*i)
    
pattern(n=int(input("Enter the number")))