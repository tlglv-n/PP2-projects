n = int(input())
for i in range(n):
   s = input()
   if "@gmail.com" in s:
      b = len(s)
      print(s[:b-10])