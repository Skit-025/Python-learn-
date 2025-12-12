def greeting(name,ending):
    msg=f"hello  wish you a very happening day !!," + name +" from the developer\n"
    print(msg+ending)
    return (name+" "+ending)           #it holds a value and returns when it is asked for by any variable
o=greeting(input("Please Enter your name :"),"Thankyou for visiting us")
print(o)