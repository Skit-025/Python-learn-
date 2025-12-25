def filter(L,word):
    l=[]
    for items in L:
        if not(items==word):
            l.append(items.strip(word))
    return l
L=["Aditya","Bobby","Chinmay","Deepak","in"]
print(filter(L,"ay"))