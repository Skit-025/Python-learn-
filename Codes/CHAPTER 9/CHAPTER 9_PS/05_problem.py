words = ["kill", "murder", "kidnap", "trap", "spoil"]
with open("censored.txt","r") as f:
    content=f.read()
    new_content=content
    for word in words:
        new_content=new_content.replace(word,"#"*len(word))
with open("censored.txt","w") as f:
    f.write(new_content)