n = int(input())
demons = {}
for i in range(n):
    s = input().split()
    if s[1] in demons:
        demons[s[1]] -= 1
    else:
        demons[s[1]] = -1
n2 = int(input())
for i in range(n2):
    s = input().split()
    if s[1] in demons:
        demons[s[1]] += int(s[2])
cnt = 0
for i in demons:
    if demons[i] < 0:
        cnt += abs(demons[i])
print("Demons left:", cnt)
