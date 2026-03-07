#EXAMPLE 1 FOR LINERN TIME COMPLEXITY
n=int(input("Enterthe range: "))
for i in range(n):
    print(i)
for i in range(n+10000):
    print(i)
for i in range(n*1000):
    print(i)
for i in range(n-500000):
print(i)
for i in range(n/100000000):
    print(i)


#EXAMPLE 2 FOR LINEAR TIME COMPLEXITY
n=int(input("Enterthe range: "))
for i in range(n):
    for j in range(10):
        print(i,j)