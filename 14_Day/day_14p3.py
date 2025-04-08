#Ejercicios dia 14 p3 

#Ejercicio 1 p3 
#Utilize el archivo countries_data.py, y realice los sig ejercicios 
print("Ejercicio 1 p3")

import countries_data as datac
data = datac.countries

#Ejercicio 1.1
#Ordenar los paises por nombre, capital y poblacion 
print("Ejercicio 1.1")
print("Por nombre:")
sortedByName = sorted(data, key = lambda x: x["name"])
for country in sortedByName:
    print(country["name"])
    
print("Por capital:")
sortedByCapital = sorted(data, key = lambda x: x["capital"])
for country in sortedByCapital:
    print(country["capital"])

print("Por población")
sortedByPopulation = sorted(data, key = lambda x: x["population"])
for country in sortedByPopulation:
    print(country['name'] , "Población:" , country['population'])
    
#Ejercicio 1.2
#Ordenalos por los diez idiomas mas hablados por hubicacion  
print("Ejercicio 1.2")
sortedLanguages = sorted(data, key=lambda x: x["population"], reverse = True)
print("Los 10 idiomas más hablados por ubicación:")
top10Spoken = sortedLanguages[:10]
for language in top10Spoken:
    print(language['languages'] , ({language['name']}) , "lo hablan:" ,  language['population'] , "habitantes")

#Ejercicio 1.3
#Ordenalos por los diez paises mas poblados 
print(" Ejercicio 1.3 ")
sortedCountries = sorted(data, key=lambda x: x["population"], reverse=True)
top10Populated = sortedCountries[:10]
print("Los 10 países más poblados son:")
for country in top10Populated:
    print(country["name"]) , country["population"]

print("revisado")