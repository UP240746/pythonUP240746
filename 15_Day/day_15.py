#Ejercicios dia 15, terminamos gracias a dios

#Ejercicio 1 
#Abra su shell interactivo python y pruebe todos los ejemplos cubiertos en esta sección
print ("Programa 1: Ejemplos")

# Prueba 1
# SyntaxError
print("Ejemplo 1: SyntaxError")
# print"Hola mundo"    # Error: Faltan los paréntesis para que se pueda imprimir.
print('Hola mundo')    


# Prueba 2
# NameError
print("Ejemplo 2: NameError")
# print(edad)     # Error: No está definida la variable.
edad = 18
print(edad)


# Prueba 3
# IndexError
print("Ejemplo 3: IndexError")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[10])     # Error: El índice está fuera de rango.
print(numeros[9])


# Prueba 4
# ModuleNotFoundError
print("Ejemplo 4: ModuleNotFoundError")
# import maths     # Error: No hay módulo llamado 'maths'.
import math


#Prueba 5
# AttributeError
print("Ejemplo 5: AttributeError")
# pi = math.PI     # Error: 'math' no tiene atributo 'PI'.
pi = math.pi
print(pi)


# Prueba 6
# KeyError
print("Ejemplo 6: KeyError")
user = {"Nombre":"Janize", "Edad":18, "Pais":"Mexico"}
# print(user[pais])     # Error: La clave es incorrecta (no está bien escrito).
print(user["Pais"])


# Prueba 7
# TypeError
print("Ejemplo 7: TypeError")
# print(5 + "7")     # Error: No se puede sumar un entero y una cadena.
print(5 + int("7"))


# Prueba 8
# ImportError
print("Ejemplo 8: ImportError")
# from math import power     # Error: No existe "power" en "math".
from math import pow
print(pow(4, 5))


# Prueba  9
# ValueError
print("Ejemplo 9: ValueError")
# print(int("7c"))     # Error: "7c" no es un número válido porque tiene la letra "c".
print(int("7"))


# prueba 10
# ZeroDivisionError
print("Ejemplo 10: ZeroDivisionError")
# print(9 / 0)     # Error: No se puede dividir por 0.
print(9 / 1)