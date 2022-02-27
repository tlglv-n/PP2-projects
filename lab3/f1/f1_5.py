<<<<<<< HEAD
def permut(n):
    for i in range(len(n)):
        for j in range(len(n)-1):
            print(*n)
            n[j], n[j+1] = n[j+1], n[j]


n = input().split()
permut(n)
=======
def permut(n):
    cnt = 0
    for i in range(len(n)):
        for j in range(len(n)-1):
            print(*n)
            n[j], n[j+1] = n[j+1], n[j]
            cnt += 1


n = input().split()
permut(n)
>>>>>>> 68ee922863d7bbad933d1b77aaeeaf5cf621a9da
