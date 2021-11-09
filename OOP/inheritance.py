class shape:
    def __init__(self):
        self.color = "Red"
        self.sides = 0
    def Area(self):
        return 0

class Quad(shape):
    def __init__(self , w , l ,c):
        self.color = c
        self.width = w
        self.length = l
        self.sides = 4
    def Area(self):
        return self.width * self.length

class square(Quad):
    def __init__(self , w , c):
        Quad.__init__(self , w , w , c)

sq1 = square(5 , "Blue")

print(sq1.Area())
print(shape.__dict__)
print(Quad.__dict__)
print(square.__dict__)
print(sq1.__dict__)

