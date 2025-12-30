class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i

    def __add__(self,other):
        real=self.r+other.r
        imag=self.i+other.i
        number=f"{real}+i{imag}"
        return number
    
    def __mul__(self,other):
#Multiplication logic(a+ib) * (c+id)= ac-bd+i(ad+bc)
        real = self.r * other.r - self.i * other.i

        imag = self.r * other.i + self.i * other.r

        number=f"{real}+i{imag}"
        return number
    def __str__(self):
        return f"{self.r}+i{self.i}"

    
a=Complex(5,6)
b=Complex(4,5)
print(a+b)
print(a*b)
