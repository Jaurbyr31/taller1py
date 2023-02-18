PesoBebe= int(input("Coloque el peso del bebe: "))
MesesBebe= int(input("Coloque los meses del bebe: "))
DosisVacuna = (((PesoBebe+10)/(MesesBebe*10))*8)

print ("la dosis debe ser: ",DosisVacuna)