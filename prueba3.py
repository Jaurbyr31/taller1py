edad=int(input("Ingresa tu edad en años \n"))
if 0<=edad<=4:
    print("El cliente ingresa gratis")
elif 4<=edad<18:
    print("El cliente debe pagar 20000")
elif 18<=edad<=60:
    print("El cliente debe pagar 15000")
else:
    print("El cliente paga 3000")