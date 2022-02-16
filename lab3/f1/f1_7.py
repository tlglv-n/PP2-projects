def thr(s):
    for i in range(1, len(s) - 1):
        if s[i] == s[i+1] == "3" or s[i] == s[i-1] == "3":
            return True
            break
    return False


s = input().split()
print(thr(s))
