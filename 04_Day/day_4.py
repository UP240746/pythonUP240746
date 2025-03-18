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

#Ejercicio 21 
#utiliza index para determinar la aparicion de P en la cadena 
print("Ejercicio 21") 
print(empresa .index("p"))

#Ejercicio22
#utiiza rfind paradetrminar la posicion de la ultima l en la frase
print("Ejercicio 22 ")
frase= "Coding For All People"
print(frase .rfind("l"))

#Ejercicio23
#Utiliza el indice o buscador para encontrar la aparicion de la palabra "because" en la sig oracion 
print("Ejercicio 23")
oracion  = 'You cannot end a sentence with because because because is a conjunction'
oracionSplit = oracion .split( )
print(oracionSplit.index("because"))

#Ejecicio24
#Usa rindex para incontrar la posicion de la aparicionde la palabra "because"en la oracion 
print("Ejercicio 24 ")
print(oracion.rindex("because"))

#Ejercicio25 
#Corta la frase "because because because" en la sig oracion
print("Ejercicio 25")
print(oracion[0:30] + oracion[54:71])

#Ejercicio26
#Encuentre la posicion en la primera aparicion de la palabra "because"
print(" Ejercico 26")
print(oracionSplit.index("because"))

#Ejercicio 27
#Corta la frase "because because because" en la sig oracion 
print("Ejeficio 27")
print(oracion[0:30] + oracion[54:71])

#Ejercicio28
#Empieza Codifi car para todos con una sub cadena codificar
print("Ejercicio 28")
print("Ejercicio 28")
print(empresa.startswith("Codificar"))

#Ejefcicio29 
#Termina la cadena subseciente codificar 
print("Ejercicio 30")
print(empresa.endswith("Codificar"))

#Ejercicio30 
#Elimina los espacios izquierdos y derechos de la cadena 
print("Ejercicio 30")
cadena = ' Codificar Para Todos  '
print(cadena.strip( ))

#Ejercicio31 
#Cual de las siguientes variables devuelve true 
print("Ejercicio 31 ")
var1 = "30DIASdePython"
var2 = "treinta_dias_de_python"
print(var1.isidentifier())
print(var2.isidentifier())

#Ejercicio32
#Unete ea las sig librerias utilizando hash o una cadena de espacios 
print("Ejercicio 32")
librerias  = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("#".join(librerias ))

#Ejercicio33
#Utiliza la secuencia de escape para separar las sigueinte soraciones
print("Ejercicio 33")
print("I am enjoying this challenge.\nI just wonder what is next.")

#Ejercicio 34
#Utiliza la secuencia tab space para ecribir las sig lineas 
print("Ejercicio 34")
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinky')

#Ejercicio 35
#Utiliza el metodo string formating para mostrar el ejercicio 
print("Ejercicio 35")
radio = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius %s is %s meters square"%(radius, area))

#Ejercicio 36 
#Utiliza el metodo string formting para el siguiente ejercicio 
print("Ejercicio 36")
a = 8
b = 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))


