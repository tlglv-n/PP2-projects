n = int(input())
for i in range(n):
   s = int(input())
   if s <= 10:
      print("Go to work!")
   elif 10 < s <= 25:
      print("You are weak")
   elif 25 < s <= 45:
      print("Okay, fine")
   elif s > 45:
      print("Burn! Burn! Burn Young!")