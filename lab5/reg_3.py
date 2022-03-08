import re
text = input()
pattern = re.findall("[a-z]+\_", text)
print(*pattern)
