#Ejercicios dia 7 parte 3 (p3)
edad = [22, 19, 24, 25, 26, 24, 25, 24]

#Ejercicio 1 p3 
#Convierte las edades en un set, compara la longitud de la lista y el set, cual es el mas grande?
print("Ejercicio 1 p3")
edades= set(edad)
print(edades )
print("longitud del det: ", len (edades))
print("Longitud de la lista: ",(edad))
if len(edades) > len(edad):
    print("La longitud del set es más grande")
else:
    print("La longitud de la lista es más grande")


#Ejercicio 2 
#Explique la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y set
print("Ejercicio 2 p3 ")
print("La funcion del string es: ")
print ("La cadena se encierra solo entre comillas y no se puede modificar después de ser creada")
print("La funcion de la lista es: ")
print("La lista es un conjunto de elementos entre corchetes, se pueden cambiar, agregar y eliminar elementos")
print("La fincion de la tupla es: ")
print("La tupla es similar a la lista, se encierra entre paréntesis y no se pueden modificar los elementos")
print("La funcion del set es: ")
print("El set es un conjunto de elementos que no se repiten pero sí se pueden modificar, se encierra entre llaves")

#Ejercicio 3 p3
#Cuantas palabras nuevas usadas en la oracion, utiliza los metodos spl
print("Ejercicio 3 p3")
fraces = "Soy un profesor, me gusta inspirar y enseñar personas"
print(fraces)
palabras= fraces.split()
palabrasUnicas = set(palabras)
print("Palabras únicas:" , len(palabrasUnicas), palabrasUnicas)
                                                                    
print("revisado")