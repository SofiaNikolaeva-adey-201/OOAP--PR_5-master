class Win_Door:
     def __init__(self, x, y):
          self.square = x * y

class Room:
    def __init__(self, x, y, z):
        self.width = x
        self.height = y
        self.lenght = z   
        self.wd = []
    def square(self):
        return 2 * self.lenght * (self.width + self.height)
    def addWD(self, w, h):
        self.wd.append(Win_Door(w, h))
    def workSurface(self):
        new_square = self.square()
        for i in self.wd:
            new_square -= i.square
        return new_square
    def roll(self, wr, hr):
        return self.workSurface()/(wr*hr)
