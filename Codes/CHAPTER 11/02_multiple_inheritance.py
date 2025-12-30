class Employee:#Main class
    company="Microsoft"
    salary=1200000
    name="toy"
    def show(self):
        print(f"The name of the employee is {self.name} and the salay is {self.salary}")
class Athlete:#2nd parent class
    sport="javlin"
    def is_athlete(self):
        self.name="harington"
        print(f"{self.name} is also a player of {self.sport}")
        
class Programmer(Athlete,Employee):#Derived class it has derived Employee and Athlete
    #It is multiple inheritance
    def expertise(self):#if i invoke is_athlete method then only the name will be overwritten else name will remain as toy
        self.language="python"
        print(f"The name of the employee is {self.name} and is good at {self.language} , his salary is {self.salary},{self.name} and is also a player of {self.sport}")
    # HERE WE USED THE CLASS ATTRIBUTES OF Employee,Athlete WITHOUT ANY PROBLEM AND THIS IS THE CONCEPT OF MULTIPLE INHERITANCE
    # SO WE CAN USE CLASS ATTRIBUTES,PROPERTIES AND METHODS OF PARENT CLASS AS WE WANT SO INHERITANCE HELPS TO REUSE CODES AND SIMPLE TO MAINTAIN  AND CHANGE -IN USE CASE
a=Employee()
b=Athlete()
c=Programmer()
c.expertise()
# print (a.company,b.company)