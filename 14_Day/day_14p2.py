#Ejercicios dia 14 p2 
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
print("Lista de países:" , countries)
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
print("Lista de nombres:" , names)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista de números:" , numbers)

#Ejercicio 1 p2 
#Utiliza el mapa para crear una nueva lista cambiando cada país a mayúsculas en la lista de países.
print("Ejercicio 1 p2 ")
print("Programa 1")
def changeToUpper(country):
    return country.upper()
countriesUpperCased = map(changeToUpper, countries)
print("Lista de países en mayúsculas:" , list(countriesUpperCased))

#Ejercicio 2 p2 
#Utiliza el mapa para crear una nueva lista cambiando cada número por su cuadrado en la lista de números
print("Ejercicio 2 p2 ")
def square(x):
    return x ** 2
numbersSquared = map(square, numbers)
print("Lista de los cuadrados de los números:" , list(numbersSquared))

#Ejercicio 3 p2 
#Utilice el map para cambiar cada nombre a mayúsculas en la lista de nombres
print("Ejercicio 3 p2")
def changeNamesToUpper(name):
    return name.upper()
namesUpperCased = map(changeNamesToUpper, names)
print("Lista de nombres en mayúsculas:" , list(namesUpperCased))

#Ejercicio 4 p2 
# Utilice el filtro para filtrar los países que contengan «land».
print("Ejercicio 4 p2 ")
def containsLand(country):
    if "land" in country:
        return True
    return False
countriesLand = filter(containsLand, countries)
print("Países que contienen la palabra 'land'" , list(countriesLand))

#Ejercicio 5 p2 
#Utilice el filtro para filtrar los países que tengan exactamente seis caracteres
print("Ejercicio 5 p2")
def isCountryLong(country):
    if len(country) == 6:
        return True
    return False
longCountries = filter(isCountryLong, countries)
print("Lista de países con 6 caracteres:" , list(longCountries))

#Ejercicio 6 p2
#Paises que contengan seis letras o mas en la lista de paises 
print("Ejercicio 6 p2 ")
def countryLong(country):
    if len(country) >= 6:
        return True
    return False
longCountries2 = filter(countryLong, countries)
print("Lista de países con 6 y más letras:" , list(longCountries2))

#Ejercicio 7 p2
#Filtrar los paises que empiezen por "E"
print("Ejercicio 7 p2")
countriesStartE = list(filter(lambda country: country.startswith("E"), countries))
print("Países que comienzan con E:" , countriesStartE)

#Ejercicio 8 p2
#Encadenar dos o más iteradores de lista (p. ej. arr.map(callback).filter(callback).reduce(callback))
print("Ejercicio 8 p2")
chainedList = list(map(str.upper, filter(lambda country: 'land' in country.lower(), countries)))
print("Países que contienen la palabra 'land' en la lista de países en mayúscula:" , chainedList)

#Ejercicio 9 p2 
#Declara una función llamada get_string_lists que toma una lista como parámetro y devuelve una lista que contiene sólo elementos de cadena.
print("Ejercicio 9 p2")
numbersAndFood = ("Soup" , "Meat" , 4 , 27 , "Nuts" , 18)
print("Lista:" , numbersAndFood)
def getStringLists(list):
    return [item for item in list if isinstance(item, str)]
print("Los elementos de cadena en la lista son:" , getStringLists(numbersAndFood))

#Ejercicio 10 p2 
#Utiliza reduce para sumar todos los números de la lista de números.
print("Ejercicio 10 p2")
result = reduce(lambda x, y: x + y, numbers)
print("La suma de los números de la lista es:" , result)

#Ejercicio 11 p2 
#Usa reduce para concatenar todos los países y producir esta sentencia: Estonia, Finlandia, Suecia, Dinamarca, Noruega e Islandia son países del norte de Europa
print("Ejercicio 11 p2 ")
concatenatedCountries = reduce(lambda x, y: x + ", " + y , countries)
print(concatenatedCountries , "are north European countries")

#Ejercicio 12 p2
#Declara una función llamada categorize_countries que devuelva una lista de países con algún patrón común (puedes encontrar la lista de países en este repositorio como countries.js(eg 'land', 'ia', 'island', 'stan')).
print("Ejercicio 12 p2 ")
import countries as c
countries2 = c.countries

def categorizeCountries(countries2, pattern):
    return list(filter(lambda country: pattern in country.lower(), countries2))
print("Países con un patrón común:" , categorizeCountries(countries2, 'land'))

#Ejercicio 13 p2
#Crea una función que devuelva un diccionario, donde las claves sean las letras iniciales de los países y los valores el número de nombres de países que empiezan por esa letra.
print("Ejercicio 13 p2")
def letterCount(countries2):
    dictionary = {}
    for country in countries2:
        initial = country[0]
        dictionary[initial] = dictionary.get(initial, 0) + 1
    return dictionary
print("La cantidad de países con cada inicial es:" , letterCount(countries2))

#Ejercicio 14 p2 
#Declara una función get_first_ten_countries: devuelve una lista de los diez primeros países de la lista countries.js de la carpeta de datos.
print("Ejercicio 14 p2 ")
def getFirstCountries(lst):
    return lst[:10]
print("los 10 primeros países de la lista son:" , list(getFirstCountries(countries2)))

#Ejercicio 15 p2 
#Declara una función get_last_ten_countries que devuelva los diez últimos países de la lista de países.
print("Ejercicio 15 p2")
def getLastTenCountries(lst):
    return lst[-10:]
print("Los últimos 10 países de la lista son:" , list(getLastTenCountries(countries2)))
