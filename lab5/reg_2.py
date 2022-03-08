import re
text = input()
matches = re.findall("abbb|abb", text)
print(*matches)
