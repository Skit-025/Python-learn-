"""Here we perform inheritance from one parent class and then that Derived class becomes the new parent class
for out child class that will derive the already derived class
let's consider we have A Manger who is a employee as well as is a programmer of a perticluar company

Employee->inherited by =>Programmer->is inherited by =>Manager

"""
class Employee:
    Company="Microsoft"
class Programmer(Employee):
    language="Python"
class Manager(Programmer):
    Department="Software world"

"""According to our expectation we will have 1 attribute for Employee 2 attribute for Programmer and 3 attribute for Manager"""
a=Employee()
b=Programmer()
c=Manager()
print(a.Company)
print(b.Company,b.language)
print(c.Company,c.language,c.Department)