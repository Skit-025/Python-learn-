class Employee:#Main class
    company="Microsoft"
    name="toy"
    salary=1200000
    language="jsp"
    def show(self):
        print(f"The name of the employee is {self.name} and the salay is {self.salary}")
# class Programmer:
#     company="ITC"
#     salary=200000
#     def show(self,):
#         print(f"The name of the employee is {self.name} and the salay is {self.salary}")
#     def expertise(self):
#         print(f"The name of the employee is {self.name} and is good at {self.language}")
class Programmer(Employee):#Derived class
    def expertise(self):
        self.language="python"
        print(f"The name of the employee is {self.name} and is good at {self.language} and his salary is {self.salary}")
    # HERE WE USED THE CLASS ATTRIBUTES OF Employee WITHOUT ANY PROBLEM AND THIS IS THE CONCEPT OF SIMPLE INHERITANCE
    # SO WE CAN USE CLASS ATTRIBUTES AND METHODS OF PARENT CLASS AS WE WANT SO INHERITANCE HELPS TO REUSE CODES AND SIMPLE TO MAINTAIN  AND CHANGE -IN USE CASE
a=Employee()
b=Programmer()
b.expertise()
b.show()
# print (a.company,b.company)