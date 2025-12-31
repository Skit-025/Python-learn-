class Number:
    def __init__(self, value):
        self.value = value

    # String representation
    def __str__(self):
        return f"Number({self.value})"

    # Addition
    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        return Number(self.value + other)

    # Subtraction
    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value)
        return Number(self.value - other)

    # Multiplication
    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value)
        return Number(self.value * other)

    # Division
    def __truediv__(self, other):
        if isinstance(other, Number):
            return Number(self.value / other.value)
        return Number(self.value / other)

    # Floor division
    def __floordiv__(self, other):
        if isinstance(other, Number):
            return Number(self.value // other.value)
        return Number(self.value // other)

    # Equality
    def __eq__(self, other):
        if isinstance(other, Number):
            return self.value == other.value
        return self.value == other

    # Less than
    def __lt__(self, other):
        if isinstance(other, Number):
            return self.value < other.value
        return self.value < other

    # Length (number of digits)
    def __len__(self):
        return len(str(abs(self.value)))


# --- Demo ---
a = Number(10)
b = Number(5)

print("a =", a)              # Number(10)
print("b =", b)              # Number(5)

print("a + b =", a + b)      # Number(15)
print("a - b =", a - b)      # Number(5)
print("a * b =", a * b)      # Number(50)
print("a / b =", a / b)      # Number(2.0)
print("a // b =", a // b)    # Number(2)

print("len(a) =", len(a))    # 2 (since "10" has 2 digits)
print("len(Number(12345)) =", len(Number(12345)))  # 5

print("a == b:", a == b)     # False
print("a < b:", a < b)       # False
print("a == 10:", a == 10)   # True
print("a + 20 =", a + 20)    # Number(30)