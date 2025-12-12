o1="Make a lot of money"
o2="Subscribe this"
o3="Click this" 
o4="buy now" 
msg=input("Enter your message:")
if((o1 in msg) or (o2 in msg) or (o3 in msg) or (o4 in msg)):
    print("spam")
else:
    print("This is not a spam")