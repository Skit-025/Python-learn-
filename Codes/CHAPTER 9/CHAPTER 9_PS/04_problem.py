def word_replacer(word):
    with open("donkey.txt","r") as f:
        content=f.read()
    new_content=content.replace(word,"######")
    with open("donkey.txt","w") as f:
        f.write(new_content)
word_replacer("donkey")