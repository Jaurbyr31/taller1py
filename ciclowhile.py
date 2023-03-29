saldo = 1000000

while True:
    print("Saldo actual:", saldo)
    opcion = input("¿Desea retirar o consignar? (r/c): ")
    if opcion.lower() == "r":
        retiro = float(input("Ingrese la cantidad a retirar: "))
        if retiro > saldo:
            print("No hay suficiente saldo disponible")
        else:
            saldo -= retiro
            print("Retiro exitoso. Saldo actual:", saldo)
    elif opcion.lower() == "c":
        consignacion = float(input("Ingrese la cantidad a consignar: "))
        saldo += consignacion
        print("Consignación exitosa. Saldo actual:", saldo)
    else:
        print("Opción inválida. Por favor, intente de nuevo.")