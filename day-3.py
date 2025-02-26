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








