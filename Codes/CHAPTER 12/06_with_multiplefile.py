with(
    open("File1.txt","w") as f1,
    open("File2.txt","w") as f2
):
    f1.write("hello world")
    f2.write("Bye world")