<<<<<<< HEAD
def filter_prime(n):
    if n < 2:
        return ""
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            return ""
    return str(n) + " "


s = input().split()
for i in s:
    print(filter_prime(int(i)), end="")
=======
def filter_prime(n):
    if n < 2:
        return ""
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            return ""
    return str(n) + " "


s = input().split()
for i in s:
    print(filter_prime(int(i)), end="")
>>>>>>> 68ee922863d7bbad933d1b77aaeeaf5cf621a9da
