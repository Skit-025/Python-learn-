class vector:
    def __init__(self,A,B,C):
            self.A=A
            self.B=B
            self.C=C

    def __add__(self,vc1,):
        X=self.A+vc1.A

        Y=self.B+vc1.B

        Z=self.C+vc1.C

        return f"Vector{X,Y,Z}"
    
    def __mul__(self,vc1,):
        X=self.A*vc1.A

        Y=self.B*vc1.B

        Z=self.C*vc1.C

        return f"{X+Y+Z}"
    def __len__(self):
        L=[self.A,self.B,self.C]
        return len(L)
    
a=vector(4,1,9)
b=vector(10,2,3)
c=vector(16,11,17)
print(a+b)
print(a*b)
print("Dimension of vector(a) =", len(a))