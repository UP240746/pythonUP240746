#Ejercicios dia 9 parte 1 (p1)

#Ejercicio 1 p1 
#Obtener la entrada del usuario mediante input para saber si tiene edad suficiente para conducir 
print("Ejercicio 1 p1")
edad= int (input("Introduce tu edad: "))
if edad >= 18: 
    print("Tienes la edad suficiente para conducir:")
else: 
    print("Tenras que esperar", 18-edad, "años para poder conducir")


#Ejercicio 2 p1 
#Compara los valores "mi edad" y "Tu edad", obtenlos usando un input
print("Ejercicio 2 p1")
miEdad= 18 
print("Mi edad es de: ", miEdad, "años")
tuEdad= int(input("Introduce tu edad: "))
if miEdad> tuEdad:
    difEdad= miEdad - tuEdad 
    if difEdad == 1:  
        print("Eres un año mayor que yo.")
    else: 
        print("Eres", difEdad, "años menor que yo.")
elif tuEdad> miEdad: 
    difEdad= tuEdad - miEdad 
    if difEdad== 1: 
        print("Eres un año mayor que yo. ")
    else: 
        print("Eres", difEdad, "años mayor que yo.  ")
else:
    print("Tenemos la misma edad")


#Ejercicio 3 p1
#Obten dos numeros del usuario y si a es mayor que b devuelve a es mayor que b, si a es menor que b devuelve a es menor que b, si no a es igual a b, salida
print("Ejercicioo 3 p1 ")
a = int(input("Ingresa un numero:  "))
b = int(input("Ingresa un numero: "))
if a > b:
    print(a , "es mayor que" , b)
elif a < b:
    print(a , "es menor que" , b)
else:
    print(a , "es igual a" , b) 

print("revisado")