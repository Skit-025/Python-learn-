class Programer:
    company="Microsoft"
    role="software developer"
    work="develop software applications"
    Salary=90000
    def __init__(self,company,role,work,Salary):
        self.company=company
        self.role=role
        self.work=work
        self.Salary=Salary
        print("Welcome to the programming world!,Created  with joy by Skit025")
        return
    def store(self):
        print("Storing data you shared...")
        with open("data_base.txt", "a") as f:
            content = f"New data\n \n Company: {self.company}\nRole: {self.role }\nWork: {self.work}\nSalary: {self.Salary}\n"
            f.write(content)
        return print("Data stored successfully!")
n=int(input("Enter number of programers you have: "))
for i in range(n+1):
    Programers=Programer(input("Enter company name: "),input("Enter role: "),input("Enter work: "),int(input("Enter Salary: ")))
    Programers.store()