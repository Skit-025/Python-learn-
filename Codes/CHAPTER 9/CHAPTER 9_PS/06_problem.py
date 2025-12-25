with open("data.txt","r") as f:
    content=f.read()
    lines=content.split(",")
    for line in lines:
        if "python" in line.lower():
            print(f"python is in line: {line}")