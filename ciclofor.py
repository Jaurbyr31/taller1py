num=int(input("Ingrese el numero \n"))
cantidad=int(input("Ingrese el limite: "))

for i in range(cantidad+1):
    res=num*i
    
    print(num, "x", i, "=", res)

