from multiprocessing.dummy import Array


s = input().split()
n = int(input())
x1 = int(s[0])
y1 = int(s[1])

arr = {}
for i in range(n):
    a = input().split()
    x2 = int(a[0])
    y2 = int(a[1])
    arr[int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)] = str(x2) + " " + str(y2)

print(arr)
