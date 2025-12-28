class handrison:
    a=11#This is a class attribute

obj=handrison()#Creating an object of the class handrison
obj.a=0#This doesn't change the class attribute, it creates an instance attribute that will be used when accessed via the object
print(obj.a)
print(handrison.a)