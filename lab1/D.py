
a = int(input())
b = input()
if b == 'k':
    c = int(input())
    print(round(float(a / 1024), c))
elif b == "b":
    print(int(a * 1024))
