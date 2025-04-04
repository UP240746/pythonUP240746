#Ejercicios dia 12 p1 
#Ejercicio 1 p1
#Escribe una función que genere un identificador de usuario aleatorio de seis dígitos/caracteres
print("Ejercicio 1 p1")
import random 
import string
def generate_random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id
print("El random user id es :", generate_random_user_id())

#Ejercicio 2 p1
#Modificar la tarea anterior. Declara una función llamada user_id_gen_by_user. 
#No toma ningún parámetro pero toma dos entradas usando input(). 
#Una de las entradas es el número de caracteres y la segunda entrada es el número de IDs que se supone deben ser generados.
print("Ejercicio 2 p1")
def user_id_gen_by_user():
    num_chars = int(input("Escribe el numero de caracteres para el identificador de usuario:"))
    num_ids = int(input("Escribe el numero de identificadores de usuario que desea generar:"))
    characters = string.ascii_letters + string.digits
    user_ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choice(characters) for _ in range(num_chars))
        user_ids.append(user_id)
    return user_ids
print("Los random user son:", user_id_gen_by_user())

#Ejercicio 3 p1 
#Escribe una función llamada rgb_color_gen. Generará colores rgb (3 valores que van de 0 a 255 cada uno).
print("Ejercicio 3 p1")
def rgb_color_gen():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)
print("El rgb colors es :", rgb_color_gen())

