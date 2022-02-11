s = list(set(input().split()))
s.sort()
print(len(s))
for i in s:
   for j in i:
      if j >= "A" and j <= "Z" or j >= "a" and j <= "z":
         print(j, end="")
   print()