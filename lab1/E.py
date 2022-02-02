def ans(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


s = input().split()
a = int(s[0])
b = int(s[1])
if a < 500 and ans(a) == True and b % 2 == 0:
    print("Good job!")
else:
    print("Try next time!")
