s = input()
n = input()
if s.find(n) == s.rfind(n):
   print(s.find(n))
else:
   print(s.find(n), end=" ")
   print(s.rfind(n))