#EJERCICIOS DIA 3 
#Declara tu edad como variable entera 

edad= 18 
print("Tu edad es: ",edad)

#Declara tu estatura como una varibale del tipo float

estatura= 1.60 # es una variable flotante por que tiene decimal 
print("Tu estatura es de:", estatura) 

#Area de un triangulo 

print("Area de un triangulo")
base= int(input("Introduce la base del triangulo:"))
altura= int(input("Introduce la altura del triangulo"))

area= ( 0.5 * base * altura )

print("El resultado es:", area )

#Perimetro de un triangulo
print("Perimetro de un triangulo")
lado_a= int(input("introduzca el lado a del triangulo: "))
lado_b=int(input("introduzca el lado b del triangulo: "))
lado_c=int(input("introduzca el lado c del triangulo:"))

perimetro= (lado_a + lado_b + lado_c) 

print("el resultado es:", perimetro)

#Longitud  y Anchura de un rectangulo 
print("Area y perimetro del rectangulo")

longitud= int(input("Introduzca la longitud del rectangulo:  "))
anchura= int(input("Inrtoduzca la ancgura del rectangulo: "))

area=(longitud * anchura)
perimetro= (2* longitud + anchura)

print("El resultado del area es: ", area )
print("El resultado del perimetro es: ", perimetro )

#Area y circunferencia de un circulo
print("Area y circunferencia del circulo")
 
radio= int(input("Introduce el radio de la circunferencia: "))
pi= 3.1416

area=(pi* radio* radio) 
circunferencia=(2 * pi * radio) 

print("El area del circulo es:  ", area )
print("La circunferencia del circulo es: ", circunferencia )

#Pendiente e intersecciones con eje x y de y=2x-2
x = 0
y = 0
interseccionEnY = (2 * x) -2
interseccionEnX = (y + 2) / 2
m = interseccionEnY / -interseccionEnX
print("La pendiente de la recta es " , m)
print("La intersección de la recta con el eje x es " , interseccionEnX)
print("La intersección de la recta con el eje y es " , interseccionEnY)

#Pendiente y distancia euclidiana entre el punto (2, 2) y el punto (6, 10)
import math
x1 = 2
y1 = 2
x2 = 6
y2 = 10
pendiente = (y2 - y1) / (x2 - x1)
distanciaEuclidiana = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("La pendiente entre los puntos es " , pendiente)
print("La distancia euclidiana entre los puntos es " , distanciaEuclidiana)

#Comparación de las pendientes de los programas 8 y 9
m1 = m
m2 = pendiente
if m1 == m2:
    resultado = "las pendientes son iguales"
else:
    resultado = "Las pendientes son diferentes"
print("La pendiente de la recta y = 2x - 2 es: " , m1)
print("La pendiente entre los puntos (2, 2) y (6, 10) es: " , m2)
print(resultado)

#Valor de y para la ecuación y = x^2 + 6x + 9
x = int(input ("inserta el valor de x: "))
y = x**2 + 6*x +9
print("El valor de y es: " , y)
if y == 0 :
    print("y es 0 cuando x es: ", x)
else:
    print("y no es 0 cuado x es: ", x)
    
#Longitud de python y dragon
pythonLen = len("python")
dragonLen = len("dragon")
comparacionFalsa = pythonLen < dragonLen
print("La longitud de 'python' es: " , pythonLen)
print("La longitud de 'dragon' es: " , dragonLen)
print("¿La longitud de 'dragon' es mayor que la de 'python'? " , comparacionFalsa)

#Sílaba "on" en python y dragon
pythonContieneOn = 'on' in 'python'
dragonContieneOn = 'on' in 'dragon'
if pythonContieneOn and dragonContieneOn:
    resultado = "La sílaba 'on' se encuentra en ambas palabras"
else:
    resultado = "La sílaba 'on' no se encuentra en ambas palabras"
print(resultado)

#jargon en oración
oracion = "I hope this course is not full of jargon"
if "jargon" in oracion:
    resultado = "La palabra 'jargon' se encuentra en la oración"
else:
    resultado = "La parabra 'jargon' no se encuentra en la oración"
print(resultado)

#No hay "on" en python ni dragon
pythonSinOn = "on" not in "python"
dragonSinOn = "on" not in "dragon"
if pythonSinOn and dragonSinOn:
    resultado = "La sílaba 'on' no se encuentra en 'dragon' ni en 'python'"
else:
    resultado = "La sílaba 'on' se encuentra en al menos una de las palabras"
print(resultado)

#Longitud de python, castear a float y string
longitudPython = len("python")
longitudPythonFlotante = float(longitudPython)
longitudPythonString = str(longitudPythonFlotante)
print("La longitud del texto 'Python' es: " , longitudPython)
print("La longitud como flotante es: " , longitudPythonFlotante)
print("La longitud como string es: " , longitudPythonString)

#Números pares divisibles entre 2
def esPar(numero):
    if numero % 2 == 0:
        return True  
    else:
        return False  
numero = int(input("Ingresa un número: "))
if esPar(numero):
    print("El número" , numero , "es par")
else:
    print("El número" , numero ,  "no es par")

#División del floor de 7 por 3 es igual al valor int convertido de 2.7
divisionFloor = 7 // 3
casteoEntero = int(2.7)
if divisionFloor == casteoEntero:
    resultado = "La división del floor de 7 por 3 es igual al valor entero de 2.7"
else:
    resultado = "La división del floor de 7 por 3 no es igual al valor entero de 2.7"
print("División del floor de 7 por 3: " , divisionFloor)
print("Valor entero de 2.7: " , casteoEntero)
print(resultado)

#Comprobar si el tipo de "10" es igual a tipo de 10
tipo10String = type("10")
tipo10Float = type(10)
if tipo10String == tipo10Float:
    resultado = "El tipo de '10' es igual al tipo de 10"
else:
    resultado = "El tipo de '10' no es igual al tipo de 10"
print("El tipo de '10' es: " , tipo10String)
print("El tipo de 10 es: " , tipo10Float)
print(resultado)

#Comprobar si int('9.8') es igual a 10
valorConvertido = int(float('9.8'))
if valorConvertido == 10:
    resultado = "int('9.8') es igual a 10"
else:
    resultado = "int('9.8') no es igual a 10"
print("int('9.8') convertido es: " , valorConvertido)
print(resultado)

#Salario de la persona
horas = float(input("Ingrese las horas trabajadas: "))
tarifaPorHora = float(input("Ingrese la tarifa por hora: "))
salario = horas * tarifaPorHora
print("El salario de la persona es de " , salario)

#Cantidad de segundos que puede vivir una persona 
años = int(input("Ingrese la cantidad de años: "))
segundosPorHora = 3600
horasPorAño = 8766
segundosTotales = años * horasPorAño * segundosPorHora
print("Una persona que viva " , años , "años puede vivir " , segundosTotales , "segundos") 
#Script que muestre la tabla
filas = 5
for num in range(1, filas + 1):
    print(num, 1, num, num**2, num**3)





