s = input()
s2 = ""
for i in range(len(s)-1, -1, -1):
    s2 += s[i]
if s == s2:
    print("It's palindrome")
else:
    print("It's not palindrome")
