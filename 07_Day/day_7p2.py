#Ejercicios dia 7 parte 2 
#sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print("Set 1:", A)
print("Set 2:", B)

#Ejercicio1 p2
#Une A y B 
print("Ejercicio 1 p2")
union= A.union(B)
print(union)

#Ejercicio2 p2
#Buscar interseccion A y B 
print("Ejercicio 2 p2")
interseccion= A.intersection(B)
print(interseccion )

#Ejercicio 3 p2 
#   Has A ub subset de B 
print("Ejercicio 3 p2")
subset= A.issubset(B)
print(subset )

#Ejercicio 4 p2 
#A y B son sets disjuntos?
print("Ejercicii 4 p2")
disjuntos= A.isdisjoint(B)
print(disjuntos)

#Ejercicio 5 p2 
#Unir A con B y B con A 
print("Ejercicio 5 p2")
unionA_B= A.union(B)
print("Union A y B: ", unionA_B)
unionB_A= B.union(A)
print("Unionn B y a: ", unionB_A)

#Ejercicio 6 p2 
#Diferencia simetrica entre Ay B 
print("Ejercicio 6 p2")
diferencia_simetrica= A.symmetric_difference(B)
print(diferencia_simetrica)

#Ejercicio 7 p2 
#Elimina los sets 
del A 
del B 
print("Los sets han sido eliminados.")
print("revisado")