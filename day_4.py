#Ejercicios dia 4 :)

#ejercicio 1 
#Concatenar la cadena de "30 dias de pytlhon" en una sola cadena 
print("Ejercicio numero 1")
n1= "Treinta"
n2= "dias"
n3= "de" 
n4= "python" 
print("Cadena:", n1 + " " + n2 +" " + n3 +" " + n4 )

#ejercicio 2
# concatenar frase 
print("Ejercicio numero 2")
n1= "Codificacion"
n2= "para"
n3= "todos"
print("cadena2:", n1 +" " + n2 +" " + n3 )

#ejercicio 3
#Declara una variable llamada empresa y asignale un valor inicial "Codificar para todos"
print("Ejercicio 3")
empresa= "Codificar para todos"
print("variable: ", empresa)

#ejercicio 4
#irmprime la variable empresa utulizndo print 
print("Ejercicio 4")
print("imprrime la variable:", empresa) 

#ejercicio 5
#imprime la  longitud de la cadena de la empresa ulilizando el metodo len() y print()
print("Ejercicio 5")
lene= len(empresa)
print(lene)

#ejercicio 6
#cambiar caracteres a mayusculas utilzando el metodo upper
print("Ejercicio 6")
caracteres= "Este texto estara en mayusculas" .upper()
print(caracteres )

#ejercicio7 
#cambiar caracteres a minusculas utilizando el metodo lower 
print("Ejercicio 7")
caracteres= "ESTE TEXTO ESTARA EN MINUSCULAS" .lower()
print(caracteres)

#Ejercicio8
#Formatear el valor de la cadena 
print("Ejercicio 8 ")
print(empresa .capitalize() )
print(empresa .title())
print(empresa .swapcase())

#ejercicio9
#corta la primera palabra de la cadena 
print("Programa 9")
cortar= empresa[0:9]
print(cortar)

#ejercicio10
#comprobar si la cadena empresa contiene un codificar  
print("Programa 10 ") 
print(empresa.find("Codificar"))
subcadena= "Codificar"
print(empresa.index(subcadena))
print("La cadena si contiene  ¨Codificar¨ en el indice 0 ")

#ejercicio 11
#Sustituye la palabra Codificra por python en la cadena 
print("Ejercicio 11")
print(empresa.replace("Codificar",  "Python"))

#Ejercicio12
#Camnie el Python para todos a Python for everyone
print("Ejercicio 12 ")
print(empresa.replace("Codificar para todos", "Python for Everyone"))

#Ejercicio13
#Divide la cadena utlizando el espacio como separardor split
print("Ejercicio 13")
print(empresa.split())

#Ejercicio14
#Dividir la cadena con comas
print("Ejercio14")
aplicaciones= "Facebook,Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(aplicaciones.split())

#Ejercicio15
#Identificar el  caracter situado en el indice 0 en la cadeana 
print("Ejercicio 15 ")
print("El caracter identificado en el indice 0 de l cadena es: ", empresa[0])

#Ejercicio16 
#Identificar el caracter situado en el ultimo indice de la cadena
print("Ejercicio 16")
print("El ultimo caracter de la cadena es: ", empresa[-1])

#Ejercicio17
# Identificar el caracter que se encunetra en el indice 10 de a cadena 
print("Ejecicio 17 ")
print("ELcaracter sutuado en el indice 10 de la cadena es: ", empresa[10] )

#Ejercicio18
#Crea un acronimo o abreviacion para el nombre de python para todos
print("Ejercicio 18 ")
nombre = "Python Para Todos"
acronimo = nombre.split()
print(acronimo[0][0] + acronimo[1][0] + acronimo[2][0])

#Ejercicio19
#Crea un acronimo para el nombre ¨Codificar para todos¨
print("Ejercicio 19 ")
nombre2= "Codificar Para Todos"
acronimo2= nombre2.split()
print(acronimo2[0][0] + acronimo2[1][0] + acronimo2[2][0])

#Ejercicio20
#Utiliza index para determinar la posicion de la primera C en la cadena
print("Ejercicio 20")
print(empresa .index("C"))