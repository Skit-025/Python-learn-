class Animals:
    print("Hey i am an Animal")
class Pet(Animals):
    print("And i could be your pet")
class Dog(Pet):
    def bark(self):
        return print("Shall i show you see bhow bhow")
a=Animals()
b=Pet()
c=Dog()
c.bark()