#print('Mi primer script de python')
#print('Ronald dale con todo no mas, vamos que vamos...')


def my_sum(*numbers):
    """
    Funcion que suma los elementos que introduzamos por parametros
    """
    result = 0
    for n in numbers:
        result += n
    return result

def my_prod(*numbers):
    """
    Funcion que multiplica los elementos que introduzamos por parametros
    """ 
    result = 1
    for n in numbers:
        result *= n
    return result

def my_description():
    print('Este modulo tiene 3 funciones: ')
    print('\t- la que muestra la descripción del módulo')
    print('\t- la que suma los números que introduzcamos por parametro')
    print('\t- la que multiplic los números que introduzcamos por parametro')

Suma_10_num = my_sum(1,2,3,4,5,6,7,8,9,10)
Mult_10_mum = my_prod(1,2,3,4,5,6,7,8,9,10)