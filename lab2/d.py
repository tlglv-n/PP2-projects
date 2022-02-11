n = int(input())
if n % 2 != 0:
   for i in range(1, n+1):
      for j in range(n-i):
         print(".", end="")
      print("#"*i)
else:
   for i in range(n - 1, -1, -1):
      for j in range(n-i):
         print("#", end="")
      print("."*i)