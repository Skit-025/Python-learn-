class Animal:
    def __init__(self,name):
        self.name=name
    def lion(self):
        return print(f"{self.name} raors")
b=Animal("Simba")
b.lion()
if __name__=="__main__":
    print("You are running this Directly.")
    print(__name__)
else:
    print("This module is imported..")