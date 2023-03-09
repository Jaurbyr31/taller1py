import random

def jugar_ppt():
    opciones = ["piedra", "papel", "tijera"]
    print("¡Bienvenido a Piedra, Papel o Tijera!")
    while True:
        print("Elige tu opción:")
        print("1 - Piedra")
        print("2 - Papel")
        print("3 - Tijera")
        print("0 - Salir")
        eleccion_usuario = input("Tu elección: ")
        if eleccion_usuario == "0":
            break
        elif eleccion_usuario in ["1", "2", "3"]:
            eleccion_usuario = opciones[int(eleccion_usuario) - 1]
            eleccion_maquina = random.choice(opciones)
            print("Tu elección: ", eleccion_usuario)
            print("La máquina elige: ", eleccion_maquina)
            if eleccion_usuario == eleccion_maquina:
                print("¡Empate!")
            elif (eleccion_usuario == "piedra" and eleccion_maquina == "tijera") or (eleccion_usuario == "papel" and eleccion_maquina == "piedra") or (eleccion_usuario == "tijera" and eleccion_maquina == "papel"):
                print("¡Ganaste!")
            else:
                print("¡La máquina gana!")
        else:
            print("Opción no válida. Por favor, introduce una opción válida (1-3) o 0 para salir.")
    print("¡Gracias por jugar!")
jugar_ppt()