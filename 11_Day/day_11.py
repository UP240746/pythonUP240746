#Ejefcicios dia 11 parte 1 (p1)

#Ejercicio 1 p1 
#Declara una funcion sumaDosNumeros, toma dos parametros y devuleve la suma 
print("Ejercicio 1 p1")
def sumaDosNumeros():
    n1= 7
    n2= 6
    total= n1 + n2
    print(total)
sumaDosNumeros()

#Ejercicio 2 p1 
# Escribe la funcion que calcule el area del circulo 
print("Ejercicio 2 p1 ")
import math 
def areaDelCirculo():
    radio= 8
    area= math.pi * radio **2
    return area 
print(areaDelCirculo())  

#Ejercicio 3 p1 
#Escribe una función llamada añadirTododslosNum que tome un número arbitrario de argumentos y sume todos los argumentos.
# Comprueba si todos los elementos de la lista son de tipo numérico.
# Si no es así da una respuesta razonable
print("Ejercicio 3 p1")
def añadirTodoslosNum(*args):
    if all(isinstance(num,(int,float)) for num in args):
        return sum(args)
    else:
        return "Error: Los argumentos debern ser numeros"
print(añadirTodoslosNum(1,2,3,4,5,6))
print(añadirTodoslosNum("string", 1,2,3))

    