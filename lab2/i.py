n = int(input())
shelf = list()
for i in range(n):
    a = input().split()
    if a[0] == "2" and shelf == []:
       continue
    if a[0] == "2":
        print(shelf[0], end=" ")
        shelf.remove(shelf[0])
    else:
        shelf.append(a[1])
