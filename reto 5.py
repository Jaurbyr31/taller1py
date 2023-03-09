import random

def calcular_descuento(total_compra, color_bolita):
    if color_bolita == "roja":
        descuento = 0.1
    elif color_bolita == "azul":
        descuento = 0.3
    elif color_bolita == "amarilla":
        descuento = 0.5
    elif color_bolita == "blanca":
        descuento = 1.0
    else:
        descuento = 0
    valor_descuento = total_compra * descuento
    total_pagar = total_compra - valor_descuento
    return valor_descuento, total_pagar

def promocion_aniversario():
    print("¡Feliz aniversario de Supermercados Noé!")
    total_compra = float(input("Ingrese el valor total de su compra: "))
    if total_compra > 50000:
        colores_bolitas = ["roja", "azul", "amarilla", "blanca"]
        bolita_obtenida = random.choice(colores_bolitas)
        print("¡Usted obtuvo una bolita de color", bolita_obtenida + "!")
        valor_descuento, total_pagar = calcular_descuento(total_compra, bolita_obtenida)
        if valor_descuento > 0:
            print("¡Felicidades! Ha obtenido un descuento del", int(valor_descuento*100), "% en su compra.")
            print("Su valor a pagar es de $", total_pagar)
        else:
            print("Lo sentimos, no ha obtenido ningún descuento.")
            print("Su valor a pagar es de $", total_compra)
    else:
        print("Lo sentimos, para obtener un descuento su compra debe ser mayor a $50.000.")

promocion_aniversario()