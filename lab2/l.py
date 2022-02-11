n = input()
for i in range(len(n)):
    if "[]" in n:
        n = n.replace("[]", "")
    elif "{}" in n:
        n = n.replace("{}", "")
    elif "()" in n:
        n = n.replace("()", "")
    else:
        break 
if n == "":
    print("Yes")
else:
    print("No")
