PRODUCTO = 10000
cantidadProductos= int(input("Coloque la cantidad de productos que va a comprar: "))
ValorPagoCliente= int(input("ingrese la cantidad que va a pagar: "))

valorCompra=(cantidadProductos*PRODUCTO)
cambio=float(valorCompra - ValorPagoCliente)

print("el cliente compra: ",cantidadProductos," producto/s")
print("Paga: ",ValorPagoCliente)

if valorCompra>ValorPagoCliente:
    print("El cliente debe: $",cambio)
else:
    cambio = ValorPagoCliente-valorCompra
    print("Se le deben devolver: $",cambio,"al cliente" )