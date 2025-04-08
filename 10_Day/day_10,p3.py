#Ejercicio sdia 10 parte 3 (p3)

#Ejercicio 1 p3 
#Ve a la carpeta de datos y utiliza el archivo countries.py, recorre los pises y extrae todos los que termienen en "land"
print("Ejercicio 1 p3")
from countries import countries
print("Paises que contienen la palabra 'land'")
for country in countries:
    if "land" in country: 
        print(country)
        
#Ejercicio 2 p3 
#invierte la lista de frutas usando el bucle
print("Ejercicio 2 p3")
print("Invertitir orden:")
frutas= ['banana', 'orange', 'mango', 'lemon'] 
for frutas in reversed (frutas):
    print(frutas)

#Ejercicio 3 p3 
#Ve a la carpeta de datos y utilize el archivo countries_data.py
print("Ejercicio 3 p3 ")
import countries_data as datac
data = datac.countries
 

#i
#Cual es el numero total de lenguas en los datos 
print("Ejercico i")
countryLanguage= []
for country in data:
    for language in country ["Lanjuages"]:
        countryLanguage.append(language)
nofLanguages= len(countryLanguage)
print("La cantidad de lenguajes en countries_data es: ", nofLanguages)

#ii
#Encuentre las 10 lenguas mas habladas a partir de los datos 
print("Ejercicios ii")
setLanguages = set(countryLanguage)
dictLanguages = {}
for language in setLanguages:
    dictLanguages[language] = 0
for language in dictLanguages:
    for country in data:  
         if language in country["languages"]:
             dictLanguages[language] = country["population"] + dictLanguages[language]
sortValuesLanguagesPopulation = sorted(dictLanguages.values(), reverse = True)
sorfKeysLanguagesPopulation = sorted(dictLanguages, key = dictLanguages.get, reverse = True)
print("Estos son los 10 idiomas mas hablados en el mundo:")
for i in range(10):
    print("Idioma:" , sorfKeysLanguagesPopulation[i] , "Las personas que hablan el idioma son:" , sortValuesLanguagesPopulation[i])
    
#iii
#Encuentre los 10 paises mas populares del mundo
print("Ejercicio iii")
countryPopulation = []
setPopulation = set(countryPopulation)
dictPopulation = {}
for country in data:
    dictPopulation[country["name"]] = country["population"]
sortedCountries = sorted(dictPopulation.items(), key = lambda x: x[1], reverse = True)
print("Los 10 países más poblados son:")
for i in range(min(10, len(sortedCountries))):
    country, population = sortedCountries[i]
    print(f"{country}: {population}")


print("revisado")