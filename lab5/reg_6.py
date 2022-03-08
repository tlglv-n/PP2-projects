import re
text = input()
pattern = re.sub("\.+|\,+|\s+", ":", text)
print(*pattern)
