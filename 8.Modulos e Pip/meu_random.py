
'''
Este módulo retorna uma lista de números aleatórios.

'''
from random import randrange

def get_random_lista(inicial, final, tam):
    '''
    Uma função que retorna uma lista de números randômicos
    '''
    lista = []
    for i in range(0,tam):
         numero = randrange(inicial, final)
         lista.append(numero)
    return lista



