<<<<<<< HEAD
def thr(s):
    for i in range(1, len(s) - 1):
        if s[i] == s[i+1] == "3" or s[i] == s[i-1] == "3":
            return True
            break
    return False


s = input().split()
print(thr(s))
=======
def thr(s):
    for i in range(1, len(s) - 1):
        if s[i] == s[i+1] == "3" or s[i] == s[i-1] == "3":
            return True
            break
    return False


s = input().split()
print(thr(s))
>>>>>>> 68ee922863d7bbad933d1b77aaeeaf5cf621a9da
