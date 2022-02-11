n = int(input())
s = input().split()
arr = []
for i in s:
   arr.append(int(i))
arr.sort()
arr.reverse()
x1 = int(arr[0])
x2 = int(arr[1])
print(x1*x2)
