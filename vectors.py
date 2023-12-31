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
    
    @classmethod
    def sum(cls, v1, v2):
        x = v1.x + v2.x
        y = v1.y + v2.y
        return cls(x,y)

    @classmethod
    def substract(cls, v1, v2):
        x = v1.x - v2.x
        y = v1.y - v2.y
        return cls(x,y)
    
    @staticmethod
    def dot_product(v1, v2):
        return (v1.x*v2.x) + (v1.y*v2.y)
    
    @staticmethod
    def distance(v1, v2):
        return math.sqrt(((v1.x-v2.x)*(v1.x-v2.x))  + ((v1.y-v2.y)*(v1.y-v2.y)))
    
    def extend_to_3D(self,z = 0):
        x = self.x
        y = self.y
        z = z
        return "({},{},{})".format(x, y, z)

class Vector3D(Vector2D):

    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z
    
    def __str__(self):
        return super().__str__()[:-1] + ',{})'.format(self.z)

    @property
    def module(self):
        square = math.sqrt((self.x*self.x) + (self.y*self.y) + (self.z*self.z))
        square = round(square, 3)
        return square

    def scalar_prod(self, n=1):
        z = n*self.z
        # Se destaca esta linea de codigo por el hecho de ahorrar codigo con el metodo super()
        return str(super().scalar_prod())[:-1] + ', {})'.format(z) 
    
    @classmethod
    def sum(cls, v1, v2):
        x = v1.x + v2.x
        y = v1.y + v2.y
        z = v1.z + v2.z
        return cls(x,y,z)
    
    @classmethod
    def substract(cls, v1, v2):
        x = v1.x - v2.x
        y = v1.y - v2.y
        z = v1.z - v2.z
        return cls(x,y,z)

    @staticmethod
    def dot_product(v1, v2):
        #return (v1.x*v2.x) + (v1.y*v2.y) + (v1.z*v2.z)
        return super().dot_product(v1,v2) + (v1.z*v2.z)
    

    @staticmethod
    def distance(v1, v2):
        return math.sqrt(((v1.x-v2.x)*(v1.x-v2.x)) + ((v1.y-v2.y)*(v1.y-v2.y)) + ((v1.z-v2.z)*(v1.z-v2.z)))
 
    @classmethod
    def zero(cls):
        x,y,z = 0,0,0
        return cls(x,y,z)
    
    @classmethod
    def horizontal(cls):
        x,y,z = 1,0,0
        return cls(x,y,z)
    
    @classmethod
    def vertical(cls):
        x,y,z = 0,1,0
        return cls(x,y,z)

    @classmethod
    def forward(cls):
        x,y,z = 0,0,1
        return cls(x,y,z)


    


