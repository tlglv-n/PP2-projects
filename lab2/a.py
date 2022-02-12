n = input().split()
i = 0
far = 0
ans = 0
while(1):
    if i == len(n):
       ans = 1
       break
    if i > far:
        ans = 0
        break
    far = max(i + int(n[i]), far)
    i += 1
print(ans)
