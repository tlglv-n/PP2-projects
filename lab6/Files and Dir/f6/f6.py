text = "abcdefghijklmnopqrstuvwxyz".upper()
for i in text:
   f = open(f"{i}.txt", "w")
   f.close()
