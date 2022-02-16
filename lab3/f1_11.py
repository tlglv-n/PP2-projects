def pal(s):
    s2 = ""
    for i in range(len(s)):
        s2 += s[i]
    if s2[::] == s2[::-1]:
        return True
    return False


s = input().split()
print(pal(s))
