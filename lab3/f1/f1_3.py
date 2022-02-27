<<<<<<< HEAD
def solve(heads, legs):
    rabbits = (legs - 2*heads) // 2  # x+y=35 and 2x+4y = 94 -> 2(35-y)+4y=94
    print("The number of rabbits is", rabbits)
    print("The number of chickens is", heads-rabbits)


heads, legs = int(input()), int(input())
solve(heads, legs)
=======
def solve(heads, legs):
    rabbits = (legs - 2*heads) // 2  # x+y=35 and 2x+4y = 94 -> 2(35-y)+4y=94
    print("The number of rabbits is", rabbits)
    print("The number of chickens is", heads-rabbits)


heads, legs = int(input()), int(input())
solve(heads, legs)
>>>>>>> 68ee922863d7bbad933d1b77aaeeaf5cf621a9da
