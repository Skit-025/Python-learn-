try:
    loop=int(input("Enter how many tables do you want: "))
    for i in range(0,loop):
        n=int(input("Enter the number you want table of: "))
        L=[f"{n}x{i}={n*i}" for i in range(1,11)]
        with open("file1.txt","a") as f:
            f.write("\n")
            f.write(str(L))
except Exception as e:
    print(e)