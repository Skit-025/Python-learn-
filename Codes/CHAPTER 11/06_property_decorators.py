"""The @property decorator in Python allows you to define class attributes with getter, setter, and deleter methods
in a clean, readable way. Its main advantages are encapsulation, readability, and flexibility
—you can control access to attributes without changing how they’re used in code."""
#Example block 1
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)

c = Circle(5)
print(c.radius)  # 5
print(c.area)    # 78.53975

#Example block 2 getter and setter

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

p = Person("Alice")
print(p.name)       # Alice
p.name = "Bob"      # Works fine
# p.name = 123      # Raises ValueError

#example 3 Getter, Setter, and Deleter

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value

    @celsius.deleter
    def celsius(self):
        print("Deleting temperature...")
        del self._celsius

t = Temperature(25)
print(t.celsius)   # 25
t.celsius = 100    # Valid
del t.celsius      # Deletes attribute