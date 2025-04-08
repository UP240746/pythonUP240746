#Ejercicios dia 12 p3 



#Ejercicio 1 p3 
#Llama a tu función shuffle_list, toma una lista como parámetro y devuelve una lista barajada
print("Ejercicio 1 p3")
def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(lst)
    return shuffled
print("La shuffled list es:", shuffle_list([1, 2, 3, 4, 5]))

#Ejercicio 2 p3
#Escribe una función que devuelva una matriz de siete números aleatorios en un rango de 0-9. Todos los números deben ser únicos. Todos los números deben ser únicos.
print("Ejercicio 2 p3")
def unique_random_numbers():
    return random.sample(range(10), 7)

# Ejemplo de su uso:
print("Los numeros random en un rango de 0-9 es:", unique_random_numbers())



 
print("revisado")