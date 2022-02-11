s = input().split()
n = int(s[0])
if len(s) == 1:
    s2 = input()
    x = int(s2)
    ans = 0
    ans2 = x
    for i in range(n):
        ans = ans ^ (x + 2*i)
    print(ans)
else:
    x = int(s[1])
    ans = 0
    ans2 = x
    for i in range(n):
        ans = ans ^ (x + 2*i)
    print(ans)
