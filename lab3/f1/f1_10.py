def unique(lst1):
    lst2 = list(dict.fromkeys(lst1))
    print(*lst2)

lst1=input().split()
unique(lst1)
