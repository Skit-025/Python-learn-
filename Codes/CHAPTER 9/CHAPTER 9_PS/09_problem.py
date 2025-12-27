with open("donkey.txt","r") as f:
    content = f.read()
    with open("donkey_copy.txt","r") as f2:
        content2 = f2.read()
        if content == content2:
            print("The contents are the same")
        else:
            print("The contents are different")