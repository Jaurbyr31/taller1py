grupo = 10
male = 0
fem = 0

for i in range(0,grupo):
    rec=(input("ingrese la letra m si es hombre y la letra f si es mujer: \n"))
    if rec =='m':
        male=male+1
    else:
        fem=fem+1

print("hay", male, "hombres y", fem, "mujeres")