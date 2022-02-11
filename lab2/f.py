n = int(input())
students = dict()
for i in range(n):
    s = input().split()
    if s[0] not in students:
        students[s[0]] = int(s[1])
    else:
        students[s[0]] += int(s[1])
sorted_students = sorted(students.keys())
max_value = max(students.values())
for i in sorted_students:
    if students[i] == max_value:
        print(i, "is lucky!")
    else:
        print(i, "has to receive", max_value - students[i], "tenge")
