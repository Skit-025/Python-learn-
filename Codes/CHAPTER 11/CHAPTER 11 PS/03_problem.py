class Employee:
    def __init__(self, salary):
        self._salary = salary
        self.increment = 0

    @property
    def salaryAfterIncrement(self):
        # Return salary after applying increment
        return self._salary + (self._salary * self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        # Decide increment based on salary
        if self._salary > 60000:
            self.increment = 7
        elif self._salary < 60000:
            self.increment = 11
        else:
            self.increment = value  # user-defined if exactly 60000

        old_salary = self._salary
        self._salary = old_salary + (old_salary * self.increment / 100)
        print(f"Salary incremented from {old_salary} to {self._salary}")


# Example usage
a = Employee(float(input("Enter your Salary: ")))
a.salaryAfterIncrement = 0   # triggers setter
print("Final Salary:", a.salaryAfterIncrement)