#Ejercicios dia 9 parte 3 (p3) 

#Ejercicio 1 p3
#Modifica el dicciionario seguun lo que se pide 
print("Ejercicio 1 p3 ")
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }}
#Verifica si la persona tiene la clave de habilidades, de ser asi imprime la habilidad 
print("Parte 1, ejercicio 1")
if "skills" in person: 
   middleSkill = person["skills"][len(person["skills"]) // 2]
   print("La habilidad que está en el centro es:" , middleSkill)  

#Compueva si la persona tiene la habilidade de paython, imprime el resultado 
print("Parte 2, ejercicio 1")
if "skills" in person:
    if "Python" in person["skills"]:
        print("La persona tiene la habilidad en 'Python")
    else:
        print("La persona no tiene la habilidad  en 'Python")

#Si las habilidades de una persona solo tienen JavaScript y React, imprime('Es un desarrollador front-end'), 
# si las habilidades de la persona tienen Node, Python, MongoDB, imprime('Es un desarrollador back-end'), 
# si las habilidades de la persona tienen React, Node y MongoDB, imprime('Es un desarrollador fullstack'), 
# si no imprime('título desconocido')
print("Parte 3, ejercicio 1")
if "skills" in person:
    if set(["JavaScript" , "React"]) == set(person["skills"]):
        print("Él es un desarrollador front end")
    elif set(["'Node' , 'Python' , 'MongoDB'"]) == set(person["skills"]):
        print("Él es un desarrollador backend")
    elif set(["React' , 'Node' , 'MongoDB"]) == set(person["skills"]):
        print(int("Él es un desarrollador fullstack"))
    else:
        print("Título desconocido")

#Si la persona esta casada y vive en finlandia, imprime la informacion en el siguente formato 
print("Parte 4, ejercicio 1 ")
if person["isMarred"] and person["country"] == "Finland":
    print(person['firstName'] , person['lastName'] , "está casado y vive en Finlandia")

print("revisado")