file=open("File1.txt","r")
data=file.read()
print(data)
file.close()
with open("Score_store.txt","r+") as f:
    f.seek(0)
    scores=f.readlines()
    print(*scores)# for testing
    print(scores==[])# for testing
    if scores==[]:
        try:
            with open("Score_store.txt","a+") as f:
                f.seek(0)
                f.write(f"{a[0]},{a[1]}\n")
                high_score=f.readline()
                print(high_score)
        except FileNotFoundError:
            print("File not found")
    else:
        pass