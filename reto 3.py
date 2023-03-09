import random
def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2


def resultado_lanzamiento(dados):
    suma = sum(dados)
    if dados[0] == dados[1]:
        if suma == 2:
            return "Has ganado con un par de unos!"
        elif suma == 12:
            return "Has ganado con un par de doces!"
        else:
            return "Has ganado con un par!"
    elif suma == 3:
        return "Has ganado con un total de tres!"
    elif suma == 11:
        return "Has ganado con un total de once!"
    elif suma == 7:
        return "Has ganado con un total de siete!"
    else:
        return "Lo siento, has perdido."

def jugar_craps():
    print("¡Bienvenido a Craps!")
    input("Presiona Enter para lanzar los dados...")
    dados = lanzar_dados()
    print("Has lanzado:", dados)
    resultado = resultado_lanzamiento(dados)
    print(resultado)

jugar_craps()
