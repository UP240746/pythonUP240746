#Ejercicios dia 14 p1 

#Ejercicio 1 p1
#Explique la diferencia entre map, filter y reduce.
print("Ejercicio 1 p1")
mapFuncion = "Toma una función y un iterable como parámetros. Devuelve un iterable con los elementos transformados."
filterFuncion = "Filtra los elementos de un iterable según una condición (devuelve True o False). Devuelve un iterable con los elementos que cumplen la condición"
reduceFuncion = "Acumula o reduce los elementos de un iterable a un solo valor mediante una función. No devuelve otro iterable, sino un único valor"
print("map:" , mapFuncion)
print("filter:" , filterFuncion)
print("reduce:" , reduceFuncion)

#Ejercicio 2 p1 
#Explicar la diferencia entre función de orden superior, cierre y decorador
print("Ejercicio 2 p1 ")
superiorFuncion = "Puede tomar una o más funciones como parámetros, puede ser devuelta como resultado de otra función, se puede modificar, se puede asignar una función a una variable"
cierreFuncion = "Es una función que 'recuerda' las variables de su entorno externo incluso después de que la función externa termine su ejecución."
decoradorFuncion = "Patrón de diseño que permite añadir nuevas funciones a un objeto existente sin modificar su estructura. Toma una función como argumento, le agrega funcionalidad y devuelve una nueva función."
print("higher order function:" , superiorFuncion)
print("closure:" , cierreFuncion)
print("decorator:" , decoradorFuncion)

#Ejercicio 3 p1 
#Definir una función de llamada antes de map, filter o reduce, ver ejemplos
print("Ejercicio 3 p1")
def doble(x):
    return x * 2
numeros = [1, 2, 3, 4, 5]
print("Lista de números:" , numeros)
numeros_dobles = map(doble, numeros)
print("Lista del doble de los números:" , list(numeros_dobles))

#Ejercicio 4 p1 
#Utilice el bucle for para imprimir cada país de la lista de países.
print("Ejercicio 4 p1 ")
print("Programa 4")
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
print("Países en la lista:")
for country in countries:
    print(country)
    
#Ejercicio 5 p1 
#Utilice for para imprimir cada nombre de la lista de nombres
print("Ejercicio 5 p1 ")
nombres = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
print("Nombres en la lista:")
for nombre in nombres:
    print(nombre)

#Ejercicio 6 p1 
#Utilize for para imprimir cada numero de la lista de numeros 
print("Ejercicio 6 p1 ")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Números en la lista:")
for numero in numeros:
    print(numero)

