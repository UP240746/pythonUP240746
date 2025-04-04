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

#Ejercicio 4 p1
#La termperatura en grados C puede ser convertida a grados F. 
#Ecribe una funcion para convertir grados C a F 
print("Ejercicio 4 p1 ")
def celcius_a_fahrenheit(celcius):
    fahrenheit= (celcius * 9 / 5 ) + 32
    return fahrenheit
print("La temperatura en Fahrenheit es:", celcius_a_fahrenheit(50))

#Ejercicio 5 p1 
#Escribe una funcion llamada comprobar_estacion, toma un parametro de mes y asignale la temporada 
print("Ejercicio 5 p1 ")
def comprobar_estacion (mes):
    if mes in ["Enero", "Febrero", "Marzo"]:
        return "invierno"
    elif mes in ["Abril","Mayo", "Junio"]:
        return "Primavera"
    elif mes in ["Julio","Agosto", "Septiembre"]:
        return "Verano"
    else: 
        return "Otoño"
print("La estacion de Enero es: ", comprobar_estacion(mes= "Enero"))


#Ejercicio 6 p1 
#Escribe una funcion llamada calcular_pendiente que devuelva la pendiente a una ecuacion lineal 
print("Ejercicio 6 p1")
print("x1=8")
print("x2= 6")
print("y1= 4")
print("y2= 2")
def calcular_pendiente(x1,x2,y1,y2):
    pen=(y2-y1) / (x2-x1)
    return pen 
print("La pendiente de la ecuacion es: ", calcular_pendiente(8,6,4,2))

#Ejercicio 7 p1 
#La ecuación cuadrática se calcula del siguiente modo: ax² + bx + c = 0. 
# Escriba una función que calcule el conjunto solución de una ecuación cuadrática
print("Ejercicio 7 p1 ")
def res_ec_cuadratica(A,B,C):
    D= B ** 2 - 4 * A * C
    if D > 0:
        x1 = (- B + D ** 0.5) / (2 * A)
        x2 = (- B - D ** 0.5) / (2 * A)
        return x1, x2 
    elif D==0: 
        x= -B/(2* A)
        return x
    else: 
        return "No hay solucion"
print("El resultado de la ecuacion cuadratica es: ", "x=", res_ec_cuadratica(1,4,8))

#Ejercicio 8 p1
#Declara una funcion llamada imprime_lista 
#Toma una lista como parametro e imprime cada elemeto de la lista 
print("Ejercicio 8 p1")
def imprime_lista(lista):
    for item in lista: 
        print(item)
marcasCarros=["Nissan", "Toyota", "Jeep", "BMW"]
print("Maracas de carros")
print(marcasCarros)

#Ejercico 9 p1 
#Declara una funcion llamada invertir_lista
#Toma un array como parametro y devuelve el inverso del array (usa bucles)
print("Ejercicio 9 p1")
print("Lista:", marcasCarros)
def invertir_lista(array):
    invertir_lista=[]
    for item in array:
        return invertir_lista
print("Invertir lista: ", invertir_lista(marcasCarros))

#Ejercicio 10 p1 
#Toma una lista como parametro y devuelve una lista de elementos en mayusculas 
print("Listas: ", marcasCarros)
def mayusculasLista(Lista):
    return [item.upper()for item in Lista]
print("Lista en mayusculas: ", mayusculasLista(marcasCarros))

#Ejercicio 11 p1 
#Declatra una funcion llamada añade_item.
#Toma como parametro una lista y un lemento, devuelve la lista con el añadido final
print("Ejeficio 11 p1 ")
def añade_item (lista, item): 
    lista.append(item)
    return lista 
print("La lista es: ",añade_item(marcasCarros, "Mercedes Benz"))

#Ejercicio 12 p1
#Declara una funcion llamada remove_item 
#Toma una lista y un elemento, devuelve  a la lista con el elemento 
print("Ejercico 12 p1")
def removeItem(lista, item):
    lista.remove(item)
    return lista 
print("La lista es: ", removeItem(marcasCarros,"BMW"))

#Ejercicio 13 p1 
#Declara la funcion sumaNumeros 
#Toma un parametro numerico y suma tdoos los numeros imares de ese rango 
print("Ejercicio 13, p1 ")
def sumaNumeros(numero):
    suma=0 
    for i in range(1 , numero +1 ):
        suma = suma +i
        return suma 
print("Suma de los numeros rango 10:", sumaNumeros(10))
        
#Ejercicio 14 
#Declara una funcion llamada sumaExtraños 
#Toma un parametro numero y suma todos los numeros impares debese rango 
print("Ejercicio 14 p1")
def suma_de_impares(n):
    suma = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            suma += i
    return suma
n = 10
resultado = suma_de_impares(n)
print("La suma de todos los números impares es: ", suma_de_impares)

#Ejercicio 15 p1 
#Toma un parametro numerico y suma todos los pares en ese rango 
print("Ejercicio 15 p1 ")
def suma_de_pares(n):
    suma = 0
    for i in range(2, n + 1, 2):
        suma += i
    return suma
n = 10
resultado = suma_de_pares(n)
print("La suma de todos los numeros pares es : ", suma_de_impares)

    