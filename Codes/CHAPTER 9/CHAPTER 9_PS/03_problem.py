def table(n):
    table=''
    for i in range(1,11):
        table+=f"{n} x {i} = {n*i}\n"
    with open(f"13_yr_old/table_of_{n}","w") as f:
        f.write(table)

for j in range(2,21):
    table(j)