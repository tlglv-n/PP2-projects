import re
text = input()
pattern = re.findall("[a-z]+[A-Z]+", text)
print(*pattern)
