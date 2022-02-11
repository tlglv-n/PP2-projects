years = []
while(1):
    s = input().split()
    if s[0] == "0":
        break
    years.append(s)
sorted_years = sorted(years, key=lambda y: [y[2], y[1], y[0]])
for i in sorted_years:
    print(*i)
