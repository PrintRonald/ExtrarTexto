import math 

class Vector2D():
    
    def __init__(self, x , y):
        self.x = x
        self.y = y
    
    @property
    def module(self):
        square = math.sqrt((self.x*self.x) + (self.y*self.y))
        square = round(square, 3)
        return square
    
    def scalar_prod(self, n = 1):
        x,y = n*self.x, n*self.y
        return x,y
    
    def __str__(self):
        return "({},{})".format(self.x, self.y)