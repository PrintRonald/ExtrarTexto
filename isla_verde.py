

class Tree():
    def __init__(self,name,height,diameter,talkative=False):
        self.name = name
        self.height = height
        self.diameter = diameter
        self.talkative = talkative
    
    def __str__(self):
        if self.talkative == True:
            return f'{self.name} es un árbol parlante que mide {self.height}cm de altura y {self.diameter}cm de díametro'
        else:
            return f'{self.name} es un árbol no parlante que mide {self.height}cm de altura y {self.diameter}cm de díametro' 
    
    def talk(self, message):
        if self.talkative == True:
            return f'{self.name} dice {message}'
        else:
            return f'{self.name} no es un árbol parlante'
    
    def grow(self,add_height=0, add_diameter = 0):
        self.height += add_height
        self.diameter += add_diameter
        return self.height, self.diameter

trees = []

def born_tree(tree_object):
    trees.append(tree_object)
    print(f'{tree_object.name} acaba de nacer')
    return tree_object.__str__()

def dead_tree(tree_object):
    if tree_object in trees:
        trees.remove(tree_object)
        print(f'{tree_object.name} ha sido eliminado del bosque.')
        return f'Descansa en paz, {tree_object.name}'
    else:
        print(f'{tree_object.name} no se encuentra en el bosque.')
    

