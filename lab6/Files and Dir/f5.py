list1 = list(input())
f = open("f5.txt", "w")
for i in list1:
    f.write(i)
f.close()
f = open("f5.txt", "r")
print(f.readlines())

