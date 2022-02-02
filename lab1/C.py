def ans(s, m):
   for i in range(len(s)):
      if s[i] >= 'A' and s[i] <= 'Z':
         m = m + chr(ord(s[i]) + 32)
      else:
         m = m + s[i]
   return m
s = input()
m = str()
print(ans(s, m))