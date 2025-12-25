#Table of a number using recursion
def table(num,n):
    if n>10:
        return
    else:
        print(f"{num} X {n} = {num*n}")
        table(num,n+1)
table(10,1)