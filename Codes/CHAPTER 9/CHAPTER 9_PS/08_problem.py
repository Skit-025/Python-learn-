with open("donkey.txt","r") as f:
    content=f.read()
    with open("donkey_copy.txt","w") as f2:
        f2.write(content)