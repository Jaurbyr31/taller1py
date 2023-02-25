count = 0
total= 0

for i in range(1,6,1):
    price=int(input("Ingrese el precio \n"))
    cantidad=int(input("Ingrese la cantidad \n"))
    count=count+1
    subtotal= price*cantidad
    total= total+subtotal

print("El total a pagar es: ", total)

rec=int(input("Ingrese valor con el que paga \n"))

if total>=rec:
    print("Debe ", total-rec)
else:
    print("Su cambio es ", rec-total)

print("se registraron", count, "referencias")

tel= input("¿cuenta con linea exito? \n")

if tel=='si':
    print("sumaste",count, "minutos a tu linea exito")
else:
    print("cambiate a nuestra linea")







