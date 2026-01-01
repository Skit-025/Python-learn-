# try:
#     with open("file1.txt") as f1:
#         content1=f1.read()
#         print(content1)
#         print(type(content1))

#     with open("file2.txt") as f2:
#         content2=f2.read()
#         print(content2)
#         print(type(content2))

#     with open("file3.txt") as f3:
#         content3=f3.read()
#         print(content3)
#         print(type(content3))

# except FileNotFoundError as e:
#     print(f"{e}")

files=["file1.txt","file2.txt","file3.txt"]
for file in files:
    try:
        with open(file) as f:
            content = f.read()
            print(content)
    except FileNotFoundError as e:
        print(e)
else:
    print("Program executed successfully..")