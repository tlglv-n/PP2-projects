def ans(s, i, dec):
   if i == len(s):
      return dec
   else:
      dec += int(s[i]) * 2**(len(s)-i-1)
   i += 1
   return ans(s, i, dec)

s = input()
print(ans(s, 0, 0))