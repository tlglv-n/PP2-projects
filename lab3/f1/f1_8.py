<<<<<<< HEAD
def spy(s):
    num = ""
    for i in s:
        if i == "0":
            num += "0"
        elif i == "7":
            num += "7"
    if "007" in num:
        return True
    return False


s = input().split()
print(spy(s))
=======
def spy(s):
    num = ""
    for i in s:
        if i == "0":
            num += "0"
        elif i == "7":
            num += "7"
    if "007" in num:
        return True
    return False


s = input().split()
print(spy(s))
>>>>>>> 68ee922863d7bbad933d1b77aaeeaf5cf621a9da
