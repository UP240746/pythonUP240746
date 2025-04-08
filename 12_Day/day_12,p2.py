#Ejercicios dia 12 p2 


#Ejercicio 1 p2
#Escribir una función lista_de_colores_hexa que devuelva cualquier número de colores hexadecimales en una lista 
#(seis números hexadecimales escritos después de #. El sistema numérico hexadecimal se compone de 16 símbolos, 0-9 y las 6 primeras letras del alfabeto, a-f).
print("Ejercicio 1 p2")
def list_of_hexa_colors(num_colors):
    hex_colors = []
    for _ in range(num_colors):
        color = '#{:06X}'.format(rand.randint(0, 0xFFFFFF))
        hex_colors.append(color)
    return hex_colors
print("La lista de hexa colors es:", list_of_hexa_colors(5))


#Ejercicio 2 p2
#Escribir una función list_of_rgb_colors que devuelva cualquier número de colores RGB en un array.
print("Ejercicio 2 p2")
def list_of_rgb_colors(num_colors):
    rgb_colors = []
    for i in range(num_colors):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        rgb_colors.append(color)
    return rgb_colors
print("La lista de rgb colors es :", list_of_rgb_colors(5))


#Ejercicio 3 p2
#Escribir una función generar_colores que pueda generar cualquier número de colores hexa o rgb.
print("Ejercicio 3 p2")
def generate_colors(num_colors, color_type):
    colors = []
    if color_type == 'hexa':
        for i in range(num_colors):
            color = '#{:06X}'.format(random.randint(0, 0xFFFFFF))
            colors.append(color)
    elif color_type == 'rgb':
        for i in range(num_colors):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            colors.append(color)
    return colors
print("La generada colors es:", generate_colors(5, 'hexa'))
print("La generada colors es:", generate_colors(5, 'rgb'))

print("revisado")