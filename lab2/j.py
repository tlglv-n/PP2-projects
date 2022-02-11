n = int(input())
s = []
for i in range(n):
    a = input()
    s.append(a)
arr = []
cnt = 0
for i in s:
    ch1 = True
    ch2 = True
    ch3 = True
    for j in i:
        if j >= "A" and j <= "Z":
            ch1 = True
            break
        else:
            ch1 = False
    for k in i:
        if k >= "a" and k <= "z":
            ch2 = True
            break
        else:
            ch2 = False
    for l in i:
        if l >= "0" and l <= "9":
            ch3 = True
            break
        else:
            ch3 = False
    if ch1 == True and ch2 == True and ch3 == True:
        arr.append(i)
arr = list(dict.fromkeys(arr))
arr.sort()
print(len(arr))
print(*arr, sep="\n")
