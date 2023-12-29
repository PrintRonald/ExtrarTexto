from isla_verde import *
# Creamos un objeto tree
#arbol = Tree('espino',30,15,False)
#arbol1 = Tree('aucalyptus',20,10,True)
#print(arbol1)
#print(arbol1.grow(5,10))
#print(arbol1.height,arbol1.diameter)
#msj = 'Hola soy un árbol muy simpatico'
#print(arbol1.talk(msj))
#arbol,arbol1,arbol2 = Tree('Boldo',1,1,False),Tree('Matico',1,1,True),Tree('Palmera',1,1,True) 
#print(born_tree(arbol))
#print(born_tree(arbol1))
#print(born_tree(arbol2))
#print(trees)
#print(dead_tree(arbol2))
#print(trees)
#print(dead_tree(arbol2))


Arbolato,Arboleto,Arbolito,Arboloto,Arboluto = Tree('Arbolato',5,2,True),Tree('Arboleto',4,1,True),Tree('Arbolito',5,1.5,True),Tree('Arboloto',5,0.5,False),Tree('Arboluto',2,0.25,False)
# Nacen 5 arbolitos
born_tree(Arbolato)
born_tree(Arboleto)
born_tree(Arbolito)
born_tree(Arboloto)
born_tree(Arboluto)
# Arbolato tiene el doble de altura y diametro
print(Arbolato.grow(5*2,2*2))
# Arboleto ha crecido solamente 3cm de altura
print(Arboleto.grow(3))
# Arbolito ha crecido 1cm en altura y 0.5 de diametro 
print(Arbolito.grow(1,0.5))
# Arboloto ha crecido solamente 3.5 cm diametro
print(Arboloto.grow(0,3.5))
# Arboluto ha crecido 0.5 cm en altura y 0.75 de diametro
print(Arboluto.grow(0.5,0.75))

# Arboluto se puso enfermo y con lo delgado que era no supero la enfermedad y murio. Descansa en paz, arboluto
print(dead_tree(Arboluto))

#  resultado = (((arbol.parlante.altura + arbol.parlante1.altura + arbol.parlante2.altura) - (arbol.Noparlante.diametro + arbol.Noparlante1.diametro)) *
#               ((arbol.parlante.diametro + arbol1.parlante.diametro + arbol2.parlante.diametro)/(arbol.Noparlante.altura + arbol1.Noparlante.altura))) + (len(lista.Tree)/2)
