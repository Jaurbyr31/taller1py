import random
valor_apuesta = 10
dinero = 100
contador_juegos = 0

while dinero > 0:
    apuesta = int(input("Ingresa la cantidad que deseas apostar: "))
    
    if apuesta > dinero:
        print("No tienes suficiente dinero para apostar esa cantidad")
        continue 
    dado = random.randint(1, 6)
    
    if dado == 1 or dado == 2:
        print(f"Perdiste, el dado sacó {dado}")
        dinero -= apuesta
        valor_apuesta = valor_apuesta // 2  

    elif dado == 3 or dado == 4:
        print(f"Empataste, el dado sacó {dado}")
        
    else:
        print(f"Ganaste, el dado sacó {dado}")
        dinero += apuesta
        valor_apuesta *= 2
    contador_juegos += 1
    
print(f"Jugaste {contador_juegos} veces y acumulaste {dinero} dólares")
