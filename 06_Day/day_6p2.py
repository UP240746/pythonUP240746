#Ejercicios dia 6, segunda parte (p2)

#Ejercicios1 p2
#Desempaquetar mi_familia 
print("Ejercicio 1 p2")
mi_familia= ("Nancy","Gabriel", "Isaias", "Angel", "Victoria")
hermanos= mi_familia[0:12]
print("Mis hermnaos: ", hermanos )
padres= mi_familia[12:0]
print("Mis padres: ", padres )

#Ejercicio2 p2
#Crea tuplas de verduras,frutas y productos de origen animal, unelas
print("Ejercicio2 p2")
frutas= ("mango", "fresa", "frambuesa", "manzana", "platano")
verduras= ("brocoli", "lechuga", "cebolla", "jitomate")
productosanimales= ("huevo","leche", "carne")
comida_tp= frutas + verduras + productosanimales
print(comida_tp)

#Ejercicio3 p2
#Cambia tu tupla a comida_il 
print("Ejercicio3 p2")
comida_tp= list("comida_it")
print(comida_tp)

#Ejercicio4 p2
#Corta los elementos centrales de la tupla
print("Ejercicio 4 p2")
print(len(comida_tp))
print(comida_tp[5],",", comida_tp[6])

#Ejercicio 5 
#Separe los primeros tres elementos y los últimos tres elementos de la lista
print("Ejercicio 5 p2")
primeros3= comida_tp [0:3]
ultimos3= comida_tp [6:10]
print("Los primeros 3 son: ", primeros3 )
print("Los ultimis 3 son: ", ultimos3 )

#Ejercicios6 p2
#Elimina la tupla por completo 
print("Ejercicios 6 p2")
del(comida_tp)
print("La tupla se elimino")

#Ejercicio7 p2
#Comprueba si existe un elemento en la tupla:
#Comprobar si Estonia es un país nórdico
#Compruebe si Islandia es un país nórdico
print("Ejercicio 7 p2")
paisesNordicos = ("Dinamarca", "Finlandia","Islandia ", "Noruega", "Suecia")
print("Tupla a comprobar:" , paisesNordicos)
#comprobar 
if "Estonia" in paisesNordicos:
    print("Estonia es un país Nórdico")
else:
    print("Estonia no es un país Nórtdico")

#comprobar2
if "Islandia" in paisesNordicos:
    print("Islandia es un país Nórdico")
else:
    print("Islandia no es un país Nórtdico")

