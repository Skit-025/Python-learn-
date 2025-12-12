tag=int(input("Enter the digit: \n"))
print(f"The table of{tag} is :\n")
for i in range(1,11):
    n=tag*i
    print(f"{tag}*{i}={n}")