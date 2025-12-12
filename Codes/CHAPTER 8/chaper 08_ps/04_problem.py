import sys
sys.setrecursionlimit(100000)
def sum(n):
    if n==1:
        return 1
    return n + sum(n-1)
n=int(input("Enter number :"))
print(f"The sum till number {n}  is :",sum(n))