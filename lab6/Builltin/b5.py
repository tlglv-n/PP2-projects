s = input().split()
s2 = list()
for i in range(len(s)):
    if s[i] == "True":
        s2.append(True)
    else:
        s2.append(False)
print(all(tuple(s2)))
