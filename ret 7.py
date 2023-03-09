import random
apuesta = 10
dinero_acumulado = 0
contador_juegos = 0

while True:
    print("Dinero disponible: ", dinero_acumulado)
    dinero_apostado = int(input("Ingrese la cantidad de dinero que desea apostar: "))

    if dinero_apostado > dinero_acumulado:
        print("No tiene suficiente dinero para apostar esa cantidad")
        continue
    
    resultado = random.randint(1, 6)
    print("Resultado del dado: ", resultado)
    
    if resultado > 3:
        
        dinero_ganado = dinero_apostado * 2
        dinero_acumulado += dinero_ganado
        apuesta = dinero_apostado
        
        print("Felicidades! Ha ganado la apuesta. Ha ganado ", dinero_ganado)
    else:
        
        dinero_perdido = dinero_apostado
        dinero_acumulado -= dinero_perdido
        apuesta = apuesta * 2
        
        print("Lo siento, ha perdido la apuesta. Ha perdido ", dinero_perdido)
    
    
    contador_juegos += 1
    
    
    continuar = input("Desea seguir jugando? (s/n) ")
    if continuar.lower() != "s":
        break


print("Ha jugado ", contador_juegos, " veces y ha acumulado un total de ", dinero_acumulado)