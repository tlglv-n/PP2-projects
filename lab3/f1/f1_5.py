def permut(n):
    for i in range(len(n)):
        for j in range(len(n)-1):
            print(*n)
            n[j], n[j+1] = n[j+1], n[j]
            cnt += 1


n = input().split()
permut(n)
