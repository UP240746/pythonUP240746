#Ejercicios dia 7 p1

#Ejercicio 1 p1 
#Hallar el conujunto del it_empresas 
print("Ejercicio 1 p1")
it_empresas= {"Facebook", "Amazon", "Google","Microsfot", "Apple", "IBM"}
print("Set:",it_empresas)

#Ejercicio2 p1 
#Añadir twitter a it_empresas
print("Ejercicio 2 p1")
it_empresas.add("Twitter")
print(it_empresas)

#Ejercicio3 p1
#Insertar varias compañias en el conjunto de it_emoresas 
print("Ejercicio 3 p1")
it_empresas.update(["Samsumg", "Toshiba", "Hp", "Dell"])
print(it_empresas)

#Ejercicio4 p1
#Elimina una de las compañias de it_empresas
print("Ejercicio 4 p1 ")
it_empresas.remove("Toshiba")
print(it_empresas)

#Ejercicio5 p1
#Cual es la diferencia entre remove and discard?
print("Ejercicio 5 p1")
it_empresas.remove ("Alcatel")
print("Al n o encintrar el elemento, lo detectara como error ")
it_empresas.discard ("Toshiba")
print("Al contrario del remove, este simplemente no hace nada al no encontrarlo")
print("revisado")