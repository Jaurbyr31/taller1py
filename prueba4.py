leche=input("¿Trajo la leche? \n Digite s o n \n")
pan=input("¿Trajo el pan? \n Digite s o n \n")
huevos=input("¿Trajo los huevos? \n Digite s o n \n")

#mama estricta
if leche=="s" and pan=="s" and huevos=="s":
    print("Era lo mínimo venga y desayuna")
else:
    print("Chanclazo")

#mama comprensiva
if leche=="s" or pan=="s" or huevos=="s":
    print("bueno")
else:
    print("ay, me va a tocar ir a mí")