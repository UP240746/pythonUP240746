print("Programa 2")
myAge = 18
print("Mi edad es de" , myAge , "años")
yourAge = int(input("Ingresa tu edad "))
if myAge > yourAge:
    ageDifference = myAge - yourAge
    if ageDifference == 1:
        print("Eres un año menor que yo")
    else:
        print("Eres", ageDifference, "años menor que yo")
elif yourAge > myAge:
    ageDifference = yourAge - myAge
    if ageDifference == 1:
        print("Eres un año mayor que yo")
    else:
        print("Eres", ageDifference, "años mayor que yo")
else:
    print("Tenemos la misma edad")
