n = int(input())
s = input().split()
arr = []
for i in s:
   arr.append(int(i))
x1 = max(arr)
for i in range(n):
   if x1 == arr[i]:
      arr[i] = 1
x2 = max(arr)
print(x1*x2)