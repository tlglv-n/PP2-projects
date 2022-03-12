s = input()
cnt_up = 0
cnt_low = 0
for i in s:
   if ord(i) >= 65 and ord(i) <= 90:
      cnt_up += 1
   if ord(i) >= 97 and ord(i) <= 122:
      cnt_low += 1
print(cnt_up, cnt_low)
