class Point:
    def __init__(self, cshow, cmove):
        self.cshow = cshow
        self.cmove = cmove

    def dist(self):
        return abs(self.cmove - self.cshow)


x = Point(int(input()), int(input()))
print(x.dist())
