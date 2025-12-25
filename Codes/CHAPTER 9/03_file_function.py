file1 = open("File1.txt", "r")

contents=file1.readlines()
print(contents)
#It returns a list of all lines in the file

content=file1.readline()
print(content)
#It returns only the first line of the file
content=file1.readline()
print(content)
#It returns second line of the file
content1=file1.readline()
print(content1)
#It returns third line of the file
content2=file1.readline()
print(content2)
#It returns fourth line of the file

file1.close()
"""
We can use readline() function with a loops also to read multiple lines. but iit is meaning less as we have readlines() function to read all lines at once.
but it can be helpfull when we are targeting a perticular line or a particular number of lines.
"""
# for example using while loop
f=open("File1.txt")
data=f.readline()
while(data!=""):
    print(data)
    data=f.readline()
f.close()