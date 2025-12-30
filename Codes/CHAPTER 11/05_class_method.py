class eight:
    section="A"
    @classmethod
    def show(cls):
        print(f"The value of section in class eight is:{cls.section}")
obj=eight()
obj.section="L" #This will ultimately fail bcz it is a class method
obj.show()