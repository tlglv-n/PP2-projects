s = input().split()
x1, y1 = int(s[0]), int(s[1])
x2, y2 = [], []
n = int(input())
for i in range(n):
   s2 = input().split()
   x2.append(s2[0])
   y2.append(s2[1])
ans = []
for i in range(n):
   ans.append(((x1-int(x2[i]))**2+(y1-int(y2[i]))**2)**0.5)
ans.sort()
for i in range(n):
   for j in range(n):
      if ((x1-int(x2[j]))**2+(y1-int(y2[j]))**2)**0.5 == ans[i]:
         print(x2[j], y2[j])
         break