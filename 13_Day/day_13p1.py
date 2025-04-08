#Ejercicios dia 13 p1 


#Ejercicio 1 p1
#Filtro sólo negative_and_zero en la lista utilizando la comprensión de la lista
print("Ejercicio 1")
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [num for num in numbers if num <= 0]
print("La lista con solo negativos y cero es:", negative_and_zero)

#Ejercicio 2 p1
#Aplanar la siguiente lista de listas de listas a una lista unidimensional.
listOfLists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print("Lista de listas:" , listOfLists)
flattenedList = [number for row in listOfLists for number in row]
flattenedList = [number for row in flattenedList for number in row]
print("Esta es la lista aplanada:" , flattenedList) 

#Ejercicio 3 p1 
# Usando comprensión de lista crea la siguiente listOfTuples:
print("Ejercicio 3")
listOfTuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(0,11)]
print("Lista generada:" , listOfTuples)

#Ejercicio 4
#Aplanar la siguiente lista a una nueva lista:
print("Ejercicio 4")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print("Lista de listas de países:" , countries)
flattenedCountries = [[country.upper(), country[:3].upper(), capital.upper()] for [(country, capital)]in countries]
print("Lista de países aplanada:" , flattenedCountries)

#Ejercicio 5 
#Cambia la siguiente lista por una lista de diccionarios:
print("Ejercicio 5")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print("Lista de listas de países:" , countries)
listDictionaries = [{'country': item[0][0].upper(), 'city': item[0][1].upper()} for item in countries]
print("Lista convertida a diccionario:" , listDictionaries)

#Ejercicio 6
#Cambia la siguiente lista de listas por una lista de cadenas concatenadas
print("Ejercicio 6 ")
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print("Lista de nombres:" , names)
concatenatedNames = [name[0][0] + " " + name[0][1] for name in names]
print("Lista de nombres concatenados:" , concatenatedNames)

#Ejercicio 7 
#Escribe una función lambda que pueda resolver una pendiente o intersección y de funciones lineales
print("Ejercicio 7")
print("Programa 7")
print("Los valores son: 3, 7, 6, 12")
slope = lambda x1, x2, y1, y2: (y2-y1)/(x2-x1)
print("La pendiente es:" , slope(3, 7, 6, 12))

print("revisado")