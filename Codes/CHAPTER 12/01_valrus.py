#Using Valrus operator
if (n := len([1,3,4,5]))>3:
    print(n)
    print(f"The list is too long ({n} elements,expected<=3)")