n = int(input())
demons = {}
hunters = {}
for i in range(n):
    s = input().split()
    if s[1] in demons:
        demons[s[1]] += 1
    else:
        demons[s[1]] = 1
n2 = int(input())
cnt = 0
for i in range(n2):
    s = input().split()
    if s[1] in hunters:
        hunters[s[1]] += int(s[2])
    else:
        hunters[s[1]] = int(s[2])
for i in demons:
    for j in hunters:
        if i == j and demons[i] <= hunters[i]:
            hunters[i] -= 1
            cnt += 1

print("Demons left:", len(demons)-cnt)
