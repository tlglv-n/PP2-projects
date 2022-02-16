def rev(s):
    rev_s = []
    for i in range(len(s)):
        rev_s.append(s[len(s)-i-1])
    return rev_s


s = input().split()
print(*rev(s))
