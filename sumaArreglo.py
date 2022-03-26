#Función que dada un arreglo de números no mayor a 1000, devuelva la suma
#Entradas: Arreglo de números random_numbers
#Salida: Suma de dicho arreglo suma

import random
def crearArreglo():
    random_numbers = [random.randint(1, 1000) for x in range(1000)] 
    '''Para modificar cuántos números queremos sumar modificar el parametro range()
       Para modificar el rango de los numeros que apareceran en la lista modificar (1, 100).
       Ejemplo:
       random.randint(1, 1000) for x in range(10000)] 
       creara una lista de 10 números enteros aleatorios entre 1 y 1000'''
    print(random_numbers)
    return random_numbers

def sumarArreglo(lista):
    x=0
    suma=0
    for x in range (len(lista)):
        suma = lista[x]+ suma
    return suma

print(sumarArreglo(crearArreglo()))
