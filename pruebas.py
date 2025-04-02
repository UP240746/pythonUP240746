# Ejercicios: Nivel 3
print("Ejercicios: Nivel 3")


# Programa 1 
# Go to the data folder and use the countries.py file. 
# Loop through the countries and extract all the countries containing the word land.
print("Programa 1")
from countries import countries
print("Países que contienen la palabra 'land'")
for country in countries:
    if "land" in country:
        print(country)


# Programa 2
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] 
# Reverse the order using loop.
print("Programa 2")
print("Orden invertido:")
fruits = ['banana', 'orange', 'mango', 'lemon'] 
for fruits in reversed(fruits):
    print(fruits)


# Programa 3
# Go to the data folder and use the countries_data.py file.
print("Programa 3")
import countries_data as datac
data = datac.countries

# Programa 3.1
# What are the total number of languages in the data
print("Programa 3.1")
countryLanguage = []
for country in data:
    for language in country['languages']:
        countryLanguage.append(language)
numberOfLanguages = len(countryLanguage)
print('La cantidades de lenguajes en countries_data es: ', numberOfLanguages)


# Programa 3.2
# Find the ten most spoken languages from the data
print("Programa 3.2")
setLanguages = set(countryLanguage)
dictLanguages = {}
for language in setLanguages:
    dictLanguages[language] = 0
for language in dictLanguages:
    for country in data:  
         if language in country['languages']:
             dictLanguages[language] = country['population'] + dictLanguages[language]
sortValuesLanguagesPopulation = sorted(dictLanguages.values(), reverse = True)
sorfKeysLanguagesPopulation = sorted(dictLanguages, key = dictLanguages.get, reverse = True)
print('Los 10 idiomas mas hablados en el mundo son (orden decreciente):')
for i in range(10):
    print("Idioma:" , sorfKeysLanguagesPopulation[i] , "Cantidad de personas que lo hablan:" , sortValuesLanguagesPopulation[i])


# Programa 3.3
# Find the 10 most populated countries in the world
print("Programa 3.3")
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
