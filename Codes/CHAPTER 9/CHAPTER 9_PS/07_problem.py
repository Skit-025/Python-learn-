with open("data.txt","r") as f:
    content=f.read()
    lines=content.split(",")
    for i,line in enumerate(lines,start=1):
        if "python" in line.lower():
            print(f"python is in line:{i}, {line}")