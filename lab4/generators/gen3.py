def my_gen(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


n = int(input())
for item in my_gen(n):
    print(item, end=" ")
