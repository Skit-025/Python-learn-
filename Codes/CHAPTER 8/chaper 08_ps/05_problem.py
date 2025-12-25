def pattern(n):
    if n<1 :return
    print('* '*n)
    pattern(n-1)
pattern(int(input("Enter number of rows: ")))