#Función que recibe de parametros x, y y devuelve la suma de x+y.
print("Ingresa \n")
x = int(input("x: "))
y= int(input("y: "))
def suma(x, y):
    return int(x+y)
    #defino como entero el retorno de la suma unicamente considerando 
    #que se solicita con una función int suma(x, y), pero si se quitará el int del return seguiría funcionando
    #porque se están pasando dos enteros
print(suma(x,y))