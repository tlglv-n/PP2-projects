<<<<<<< HEAD
def pal(s):
    s2 = ""
    for i in range(len(s)):
        s2 += s[i]
    if s2[::] == s2[::-1]:
        return True
    return False


s = input().split()
print(pal(s))
=======
def pal(s):
    s2 = ""
    for i in range(len(s)):
        s2 += s[i]
    if s2[::] == s2[::-1]:
        return True
    return False


s = input().split()
print(pal(s))
>>>>>>> 68ee922863d7bbad933d1b77aaeeaf5cf621a9da
