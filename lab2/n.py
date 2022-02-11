a = int(input())
arr = []
while a != 0:
    arr.append(a)
    a = int(input())
for i in range(len(arr)//2):
    print(arr[i] + arr[-i-1], end=" ")
    if len(arr) % 2 != 0 and i + 1 == len(arr)//2:
        print(arr[i+1])
