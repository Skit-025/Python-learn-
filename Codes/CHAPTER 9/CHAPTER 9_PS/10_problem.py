def wipe(file):
    with open(file,"w+") as f:
        f.seek(0)
        f.write("")
wipe("donkey_wiped.txt")