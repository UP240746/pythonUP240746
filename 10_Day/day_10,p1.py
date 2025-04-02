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

#Ejercicio 4 p1 
#Utiliza bucles anindados para crar lo que te piden 
print("Ejercicio 4 p1")
b= 8
c= 8
for j in range(b):
    for i in range(c):
        print("#", end="")
        print()
        
#Ejercicio 5 p1
#Imprime el siguiente patron
print("Ejercicio 5 p1")
for d in range(11): 
    print(d,"x", d, "=", d * d)
    
#Ejercicio 6 p1
#Iterar a traves de la lista python 
print("Ejercicio 6 p1")
lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in lista:
    print(item)

#Ejercicio 7 p1 
#Usa el bucle for para iterar de 0 a 100 e imprime solo numeros extraños
print("Ejercicio 7 p1")
for f in range (101):
    if (f % 2==0 ):
        print(f) 

#Ejercicio 8 p1
#Utiliza el bucle for para iterar de 0 a 100 e imprime la suma de todos los numeros
print("Ejercicio 8 p1 ")
for p in range(100):
    if (p % 2 == 0):
        p = p + 1
        print(p)