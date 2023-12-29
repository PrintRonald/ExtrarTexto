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


Arbolato,Arboleto,Arbolito,Arboloto,Arboluto = Tree('Arbolato',5.0,2.0,True),Tree('Arboleto',4.0,1.0,True),Tree('Arbolito',5.0,1.5,True),Tree('Arboloto',5.0,0.5,False),Tree('Arboluto',2.0,0.25,False)
print('5 árboles nacen en esta isla')
print(f'En mi lista de arboles hay {len(trees)} arboles')
born_tree(Arbolato)
print(Arbolato)
print('--/--/--/--/--/--/--/--/--/--/')
born_tree(Arboleto)
print(Arboleto)
print('--/--/--/--/--/--/--/--/--/--/')
born_tree(Arbolito)
print(Arbolito)
print('--/--/--/--/--/--/--/--/--/--/')
born_tree(Arboloto)
print(Arboloto)
print('--/--/--/--/--/--/--/--/--/--/')
born_tree(Arboluto)
print(Arboluto)
print('--/--/--/--/--/--/--/--/--/--/')
print(f'En mi lista de arboles hay {len(trees)} arboles')
print('--/--/--/--/--/--/--/--/--/--/')
print('Arbolato ha crecido el doble de altura y diametro')
print(Arbolato.grow(5,2))
print('Actualmente: ')
print(Arbolato)
print('--/--/--/--/--/--/--/--/--/--/')
print('Arboleto ha crecido solamente 3cm de altura')
print(Arboleto.grow(3))
print('Actualmente: ')
print(Arboleto)
print('--/--/--/--/--/--/--/--/--/--/')
print('Arbolito ha crecido 1cm en altura y 0.5 de diametro')
print(Arbolito.grow(1,0.5))
print('Actualmente: ')
print(Arbolito)
print('--/--/--/--/--/--/--/--/--/--/')
print('Arboloto ha crecido solamente 3.5 cm diametro')
print(Arboloto.grow(0,3.5))
print('Actualmente: ')
print(Arboloto)
print('--/--/--/--/--/--/--/--/--/--/')
print('Arboluto ha crecido 0.5 cm en altura y 0.75 de diametro')
print(Arboluto.grow(0.5,0.75))
print('Actualmente: ')
print(Arboluto)
print('--/--/--/--/--/--/--/--/--/--/')
print(f'Arboluto se puso enfermo y con lo delgado que era no supero la enfermedad y murio...')
print(dead_tree(Arboluto))
print('--/--/--/--/--/--/--/--/--/--/')
print(f'Ahora en mi lista de arboles hay {len(trees)} arboles')

#  resultado = (((arbol.parlante.altura + arbol.parlante1.altura + arbol.parlante2.altura) - (arbol.Noparlante.diametro + arbol.Noparlante1.diametro)) *
#               ((arbol.parlante.diametro + arbol1.parlante.diametro + arbol2.parlante.diametro)/(arbol.Noparlante.altura + arbol1.Noparlante.altura))) + (len(lista.Tree)/2)
#print("",Arbolato,"\n",Arboleto,"\n",Arbolito,"\n",Arboloto,"\n",Arboluto)


# Arboles parlantes v/s arboles No parlantes 
ArbolParlanteList = []
ArbolNoParlanteList = []
for Arbol in trees:
    if (Arbol in trees) and (Arbol.talkative == True):
        print(Arbol.talkative)
        ArbolParlanteList.append(Arbol)
    else:
        ArbolNoParlanteList.append(Arbol)
print(ArbolNoParlanteList)
print(ArbolParlanteList)
# suma de las alturas de los árboles parlantes menos el diámetro total de los árboles no parlantes de la lista trees
totalAlturaAP = 0.0
for arbolParlante in ArbolParlanteList:
    totalAlturaAP += arbolParlante.height
print(f'La suma total de altura de los arboles parlantes es igual a : {totalAlturaAP}')
totalDiametroANP = 0.0
for arbolNoParlante in ArbolNoParlanteList:
    totalDiametroANP += arbolNoParlante.diameter
print(f'La suma total de diametros de arboles NO parlantes es igual a : {totalDiametroANP}')
Diferencia = totalAlturaAP - totalDiametroANP
print(f'{totalAlturaAP} menos {totalDiametroANP} es igual a {Diferencia}')
# cociente de la división de la suma de los diámetros de los árboles parlantes entre la altura total de los árboles no parlantes de la lista trees
totalDiametroAP = 0.0
for arbolParlante in ArbolParlanteList:
    totalDiametroAP += arbolParlante.diameter
print(f'La suma de diametros de los arboles parlantes es igual a: {totalDiametroAP}')
totalAlturaANP = 0.0
for arbolNoParlante in ArbolNoParlanteList:
    totalAlturaANP += arbolNoParlante.height
print(f'La suma de altura de los arboles NO parlantes es igual a: {totalAlturaANP}')
Division = totalDiametroAP/totalAlturaANP
print(f'{totalDiametroAP} dividido {totalAlturaANP} es igual a {Division}')
#  a los resultados anteriores los debo multiplicar
multiplicar = Diferencia * Division
print(f'El resultado de multiplicar {Diferencia} por {Division} es {multiplicar}')
#  Al resultado anterior, súmale la mitad de la longitud de la lista trees"
longListaTrees = len(trees)/2
print(f'La mitad de la longitud de la lista trees es igual a: {longListaTrees}')
ResultadoFinal = multiplicar + longListaTrees
print(f'El resultado final del acertijo es: {ResultadoFinal}')


# El primer resultado me da 45.2

# El segundo me da 28.599999999999998
