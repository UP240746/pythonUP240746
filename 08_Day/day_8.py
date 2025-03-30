#Ejercicios dia 8 

#Ejercicoo 1 
#Crea un diccionario  vacio llamado perro 
print("Ejercicio 1")
perro={}
print(len(perro))

#Ejercicio 2
#Añade nombre, color, raza, peirna, edad al diccionario del perro 
print("Ejercicio 2")
perro= {
    "Nombre" : "Stephy", 
    "Color" : "Marron ",
    "Raza" : "Boxer",
    "Piernas" : "4",
    "Edad" : "8", 
}
print(perro)

#Ejercicio 3
#Crea un diccionario de estudiante y añade ndus datos personales como como claves del diccionario 
print("Ejercicio 3")
estudiante = {
    "Nombre" : "Janize",
    "Apellido" : "Marquez ",
    "Genero" : "Mujer",
    "Edad" : "18",
    "Estado civil" : "Soltera",
    "Habilidades": ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 
    "Pais" : "Mexico ",
    "Ciudad": "Aguasacalientes", 
    "Direccion" : "Avenida ayuntamiento 1K"    
}
print(estudiante)

#Ejercicio 4
# Longitud del duccionario del estudiante 
print("Ejercicio 4 ")
print (len(estudiante))

#Ejefcicio 5 
#Evaliua las habilidades y checa el tipo de datos, deberia ser una lista 
print("Ejercicio 5 ")
evaluarHabilidades= estudiante["Habilidades"]
print(evaluarHabilidades)
print(type(evaluarHabilidades))

#Ejercicio 6 
# Modifica las habilidade y añade dos o tres habilidades
print("Ejercicio 6 ")
estudiante["Habilidades"].append('HTML')
estudiante["Habilidades"].append('C++')
print(estudiante)

#Ejercicio 7
#Obtener las llaves del diccionario como una lista 
print("Ejercicio 7")
llavesL= estudiante.keys()
print("Llaves de la lista: ", llavesL)

#Ejercicio 8 
#Obtener los valores del diccionario como una lista
print("Ejercicio 8 ")
valoresL= estudiante.values()
print("Valores de la lista: ", valoresL)

#Ejercicio 9 
#Cambia el diccionario a una lsta de tuplas utilizando el metdodo items()
print("Ejercicio 9 ")
tuplaL= estudiante.items()
print("Lista tuplas: ", tuplaL)

#Ejercicio 10 
#Elimina uno de los items del diccionario 
print("Ejercicio 10")
estudiante.popitem()
print(estudiante)

#Ejercicio 11 
#Elimina uno de los diccionarios 
print("Ejercicio 11")
del estudiante 
print("Se elimino el diccionario estudiante. ")

