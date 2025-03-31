#Ejercicios dia 9 parte 2 (p2)

#Ejercicio 1 p2 
#Escribe un codigo donde califiques a los alumnos segun sus puntuaciones
# A= 90-100
# B= 70-89
# C=60-69
# D=50-59
# F=0-49
print("Ejercicio 1 p2 ")
puntuacion= int(input("Introduzca la puntuacion del alumno:"))
if 90<= puntuacion <=100: 
    cal= "A"
    print("La calificacion del alumno es:", cal)
elif 70<= puntuacion <= 89:
    cal="B"
    print("La calificacion del alumno es:", cal)
elif 60<= puntuacion <= 69:
    cal="C"
    print("La calificacion del alumno es:", cal)
elif 50<= puntuacion <= 59:
    cal="D"
    print("La calificacion del alumno es:", cal)
else: 
    cal="F"
    print("La calificacion del alumno es:", cal)

#Ejercicio 2 p2 
#Comprueva si la estacion es primavera, verano, otoño o invierno 
print("Ejercicio 2 p2")
mes = input("Ingresa un mes: ")
if mes in ("Septiembre", "Octubre", "Noviembre"):
    estacion = "Otoño"
    print("La estación para", mes, "es", estacion)
elif mes in ("Diciembre", "Enero", "Febrero"):
    estacion = "Invierno"
    print("La estación para", mes, "es", estacion)
elif mes in ("Marzo", "Abril", "Mayo"):
    estacion = "Primavera"
    print("La estación para", mes, "es", estacion)
else:
    mes in ("Junio", "Julio", "Agosto")
    estacion = "Verano"
    print("La estación para", mes, "es", estacion)

#Ejercicio 3 p2
# De la lista de frutas si una fruta no existe, añadela e imrpime la lista modificada, si ya existe impeime que ya existe
print("Ejercicio 3 p2")
frutas = ['platano', 'naranja', 'mango', 'limon']
AñadirF= input("Ingresa una fruta (iniciando con minúscula): ")
if AñadirF in frutas:
    print('Esa fruta ya existe en la lista')
else:
    frutas.append(AñadirF)
    print("Lista modificada: ", frutas)
    

