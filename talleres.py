notas = 4
total = 0

for i in range(notas):
    nota=int(input("ingrese la nota obtenida: \n"))
    total+=nota

promedio = total/4
print("Su promedio es de: ", promedio)

if 0 <= promedio >= 0:
    print("Su promedio es de: ", promedio)
elif 3.0<= promedio <= 3.9:
    print("Su promedio es de: ", promedio)
elif 4.0<= promedio <= 4.5:
    print("Aprobó con un ")
elif promedio >= 4.5:
    print("Su promedio es de: ", promedio)