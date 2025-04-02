#Ejercicios dia 10 parte 2 (p2)

#Ejercicio 1 p2 
#Usa el bucle for para iterar de 0 a 100 e imprime la suma de todos los numeros 
print("Ejercicio 1 p2")
numero= 0 
suma = 100 
while numero <= 100:
    suma= suma + numero 
    numero += 1 
    print("La suma de los numeros es: ", suma )
    
#Ejercicio 2 p2 
# Usa el bucle for para iterar de 0 a 100 e imprime la suma de todos los eventos de numeros extraños 
print("Ejercicio 2 p2")
eventos= 0 
extraños= 0 
for n in range(100): 
    if n%2==0:
        eventos= eventos+n 
    else: 
        extraños = extraños + n 
print("La suma de todos los pares es de: ", eventos)
print("La suma de todos los extraños es: ", extraños)
