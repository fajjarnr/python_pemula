class induk:
    def __init__(self, x):
        self.x = x
    def printx(self):
        print("Nilai x : %d" % self.x)

class anak(induk):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
    def printy(self):
        print("Nilai y : %d" % self.y)
    def printxy(self):
        super().printx()
        self.printy()

obj = anak(100, 200)
obj.printxy()