#Ejercicios dia 10 parte 1, (p1)
 
#Ejercicio 1 p1 
#ilterar de 0 a 10 ultilizando el bucle for, hacer los mismo utilizando el bucle while 
print("Ejercicio 1 p1")
print("Bucle While:")
i=0 
while i <11:
    print(i)
    i= i+1 
    print("Bucle For: ")
for i in range (11):
    print(i)

#Ejercicio 2 p1 
#literar de 10 a 0 usando el bucle for, hacer lo mismo con el bucle while 
print("Ejercicio 2 p1")
print("Bucle While")
i2= 10 
while i2> 0:
    print(i2)
    i2= i-1
print("Bucle For: ")
for i2 in range (10, -1,-1):
    print(i2)
    
#Ejercicio 3 p1
#Escribe un bucle que haga 7 llamadas a print, de forma que obtengamos un triangulo 
print("Ejercicio 3 p1")
print("Con bucle for:")
for a in range (1,8):
    print("#"*a)
    
print("Con bicle while:  ")
a=1 
while a<= 7:
    print("#"*a)
    a=a+1    

