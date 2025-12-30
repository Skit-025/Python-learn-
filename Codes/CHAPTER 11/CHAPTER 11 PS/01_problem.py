class vector_2D:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def call(self):
        return print(f"{self.n1}i + {self.n2}j")
class vector_3D(vector_2D):
    def __init__(self, n1, n2,n3):
        super().__init__(n1, n2)
        self.n3=n3
    def call(self):
        return print(f"{self.n1}i + {self.n2}j + {self.n3}k")



obj1=vector_2D(input("Enter n1: "),input("Enter n2: "))
obj1.call()

obj2=vector_3D(input("Enter n1: "),input("Enter n2: "),input("Enter n3: "))
obj2.call()