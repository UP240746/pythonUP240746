#Ejercicios dia 11 parte 3 p3 

#Ejercicio 1 p3 
#Escribe una función llamada es_primo, que compruebe si un número es primo.
print("Ejercicio 1 p3")
def primo(sum):
   if sum in (0,1):
      return False
   for i in range(2, int(sum**0.5) + 1):
      if sum % i == 0:
         return False
      return True 
   sum = int(input("Escribe un numero:"))
if primo(sum):
    print(f"{sum} es un número primo.")
else :
    print(f"{sum} no es un número primo.")
    

#Ejercicio 2 p2 
#Escribe una función que compruebe si todos los elementos de la lista son únicos.
print("Ejercicio 2 p3")
def elementosUnicos(lista):
    return len(lista) == len(set(lista))
    
mi_lista = [1, 2, 3, 4, 5]
if elementosUnicos(mi_lista):
        print("Todos los elementos son únicos.")
else:
        print("Hay elementos repetidos en la lista.")
#Ejercicio 3 p3 
#Escribe una función que compruebe si todos los elementos de la lista son del mismo tipo de datos.
print("Ejercicio 3 p3")
def mismosDatos(lista):
    if len(lista) == 0:
        return True
    tipo = type(lista[0])
    for elemento in lista:
        if type(elemento) != tipo:
            return False
    return True
mi_lista = [1, 2, 3, 4, 5]
if mismosDatos(mi_lista):
        print("Todos los elementos son del mismo tipo de dato.")
else:
        print("Los elementos no son del mismo tipo de dato.")


#Ejercicio 4 p3
#Escribe una función que compruebe si la variable proporcionada es una variable python válida.
print("Ejercicio 4 p3 ")
def variableValida(variable):
    import re
    return bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', variable))
variable = input("Escribe una variable:")
if variableValida(variable):
        print(f"{variable} es una variable válida.")
else:
        print(f"{variable} no es una variable válida.")


#Ejercicio 5 p3 
#Ve a la carpeta data y accede al fichero countries-data.py.
#Crea una función llamada idiomas_más_hablados_en_el_mundo. Debe devolver 10 o 20 idiomas más hablados en el mundo en orden descendente
#Crea una función llamada países_más_poblados. Debe devolver 10 o 20 países más poblados en orden descendente.
print("Ejercicio 5 p3")

import countries_data as datac
data = datac.paises

print("Ejercicio 5.1")
from collections import Counter
def mostSpokenLanguages (dict):
     allLanguages = [lang for country in dict for lang in country['languages']] 
     cout = Counter(allLanguages)
     top10 = cout.most_common(10)
     return top10
print("Los 10 idiomas más hablados son:" , mostSpokenLanguages(data))

print("Ejercicio 5.2")

def mostPopulatedCountries (dict):
     most_populated = []
     top_10Countries = sorted(dict, key=lambda x: x["population"], reverse=True)[:10]
     print('Los 10 países más poblados son:')
     for country in top_10Countries:
         most_populated.append(f"{country['name']} - {country['population']}")
     return most_populated
print(mostPopulatedCountries(data))
