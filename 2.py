saldo = 4500
intentos = 3
import random

while intentos > 0:
    numero_celular = input("Ingrese su número de celular: ")
    clave = input("Ingrese su clave de 4 dígitos: ")

    if numero_celular == "1234567890" and clave == "1234":
        print("Bienvenido a Nequi Colombia")
        print(f"Saldo disponible: ${saldo}")
        break
    else:
        intentos -= 1
        if intentos == 0:
            print("¡Upps! Parece que tus datos de acceso no son correctos")
            break
        else:
            print(f"¡Upps! Parece que tus datos de acceso no son correctos, "
                  f"Tienes {intentos} intentos más.")

while True:
    print("Seleccione una opción:")
    print("1. Sacar")
    print("2. Envíar")
    print("3. Recargar")
    print("4. Salir")

    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        if saldo < 2000:
            print("No te alcanza para hacer el retiro.")
        else:
            print("Seleccione una opción:")
            print("1. Cajero")
            print("2. Punto físico")
            opcion_retiro = input()

            if opcion_retiro == "1" or opcion_retiro == "2":
                monto_retiro = int(input("Ingrese el monto a retirar: "))
                if monto_retiro > saldo:
                    print("No tienes suficiente saldo para hacer el retiro.")
                else:
                    saldo -= monto_retiro
                    print(f"Retiro de ${monto_retiro} exitoso.")
                    codigo_retiro = str(random.randint(100000, 999999))
                    print(f"Su código de retiro es: {codigo_retiro}")
            else:
                print("Opción inválida.")



    elif opcion == "2":
        numero_destino = input("Ingrese el número de teléfono al que desea enviar dinero: ")
        valor_envio = int(input("Ingrese el valor a enviar: "))
        if valor_envio > saldo:
            print("No tienes suficiente saldo para hacer el envío.")
        else:
            saldo -= valor_envio
            print(f"Envío de ${valor_envio} a {numero_destino} exitoso.")



    elif opcion == "3":
        valor_recarga = int(input("Ingrese el valor a recargar: "))
        confirmacion = input(f"¿Está seguro que desea recargar ${valor_recarga}? (s/n): ")
        if confirmacion == "s":
            saldo += valor_recarga
            print("Recarga exitosa.")
        else:
            print("Recarga cancelada.")


    elif opcion == "4":
        print("Gracias por usar Nequi Colombia.")
        break

    else:
        print("Opción inválida.")
        
    print(f"Su saldo disponible es: ${saldo}")

    opcion_continuar = input("¿Desea realizar alguna otra acción? (s/n): ")
    if opcion_continuar.lower() == "n":
        print("Gracias por usar Nequi Colombia.")
        break