#Ejercicios dia 11 parte 2, p2


#Ejercicio 1 
#Declare una función llamada pares_y_probabilidades . 
# Toma un entero positivo como parámetro y cuenta el número de pares y probabilidades en el número. Toma un parámetro numérico y suma todos los números pares en ese - rango.
print("Ejercicio 1 p2:")
def paresProbabilidades(numero):
    pares = 0
    impares = 0
    for i in range(1, numero + 1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares
numero = int(input("Escribe un número positivo: "))
pares, impares = paresProbabilidades(numero)
print(f"El número de pares es: {pares}")
print(f"El número de impares es: {impares}")

#Ejercicio 1.2 p2 
#Llama a tu función factorial, toma un número entero como parámetro y devuelve un factorial del número
print("Ejercicio 1.2 p2")
def factorial(numero):
    if numero < 0:
        return "Error: El factorial no está definido para números negativos."
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado
numero = int(input("Escribe un número entero: "))
print(f"El factorial de {numero} es: {factorial(numero)}")

#Ejercicio 2 p2 
#Llama a tu función vacio, toma un parámetro y comprueba si está vacío o no
print("Ejercicio 2 p2")
def vacio(parametro):
    return not bool(parametro)
parametro = input("Escribe algo (o no): ")
if vacio(parametro):
    print("El parámetro está vacío.")
else:
    print("El parámetro no está vacío.")

#Ejercicio 3 p2
#Deberían calcular_media, calcular_mediana, calcular_modo, calcular_rango, calcular_varianza, calcular_std (desviación estándar).
print("Ejercicio 3 p2")
def calcularMedia(lista):
    return sum(lista) / len(lista)
def calcularMediana(lista):
    lista.sort()
    n = len(lista)
    if n % 2 == 0:
        return (lista[n//2 - 1] + lista[n//2]) / 2
    else:
        return lista[n//2]
def calcularMode(lista):
    from collections import Counter
    contador = Counter(lista)
    max_count = max(contador.values())
    modes = [num for num, count in contador.items() if count == max_count]
    return modes if len(modes) > 1 else modes[0]
def calcularRango(lista):
    return max(lista) - min(lista)
def calcularVarianza(lista):
    mediana = calcularMedia(lista)
    return sum((x - mediana) ** 2 for x in lista) / len(lista)
def calcular_std(lista):
    return calcularVarianza(lista) ** 0.5
datos = [1,2,3,4,5,6,7,8,9,10]
media = calcularMedia(datos)
mediana = calcularMediana(datos)
modo = calcularMode(datos)
range_value = calcularRango(datos)
varianza = calcularVarianza(datos)
std_dev = calcular_std(datos)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", modo)
print("Rango:", range_value)
print("Varianza:", varianza)
print("Desviación estándar:", std_dev)


print("revisado")