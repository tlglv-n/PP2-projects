def ans(n):
   for i in n:
      


s = input().split("+")
x1 = str()
x2 = str()
if "ONE" in s[0]:
    x1 += '1'
elif "ONE" in s[1]:
    x1 += '1'
if "TWO" in s[0]:
    x1 += '2'
elif "TWO" in s[1]:
    x2 += '2'
if "THR" in s[0]:
    x1 += '3'
elif "THR" in s[1]:
    x2 += '3'
if "FOU" in s[0]:
    x1 += '4'
elif "FOU" in s[1]:
    x2 += '4'
if "FIV" in s[0]:
    x1 += '5'
elif "FIV" in s[1]:
    x2 += '5'
if "SIX" in s[0]:
    x1 += '6'
elif "SIX" in s[1]:
    x2 += '6'
if "SEV" in s[0]:
    x1 += '7'
elif "SEV" in s[1]:
    x2 += '7'
if "EIG" in s[0]:
    x1 += '8'
elif "EIG" in s[1]:
    x2 += '8'
if "NIN" in s[0]:
    x1 += '9'
elif "NIN" in s[1]:
    x2 += '9'
print(int(x1)+int(x2))