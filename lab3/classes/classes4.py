<<<<<<< HEAD
class Point:
    def __init__(self, cshow, cmove):
        self.cshow = cshow
        self.cmove = cmove

    def dist(self):
        return abs(self.cmove - self.cshow)


x = Point(int(input()), int(input()))
print(x.dist())
=======
class Point:
    def __init__(self, cshow, cmove):
        self.cshow = cshow
        self.cmove = cmove

    def dist(self):
        return abs(self.cmove - self.cshow)


x = Point(int(input()), int(input()))
print(x.dist())
>>>>>>> 68ee922863d7bbad933d1b77aaeeaf5cf621a9da
