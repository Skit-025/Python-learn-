a=99
def glob():
    global a
    a=76
    print(a)
glob()
print(a)