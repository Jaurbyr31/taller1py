class Animal:
    #Atributos
    nombre=""
    
    edad=0

    #Metodos
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad


    #Definición o declaración método convencional
    def registrarAnimal(self):
        self.nombre=input("Ingrese el nombre del animal: ")
        self.edad=int(input("Ingrese la edad del animal: "))
        
    #metodo con parametros
    '''def mostrarAnimal(self, nombre, edad):
        print ("El nombre del animal es", nombre, "y la edad es", edad)
        print (f"El nombre del animal es {nombre} y la edad es {edad}")'''
    
    def mostrarAnimal(self):
        print (f"El nombre del animal es {self.nombre} y la edad es {self.edad}")


    #método con valor retorno
    def duplicarEdad(self, edad):
        duplicado=edad*2
        return duplicado


#Crear objeto
guacamayo=Animal("", 0)

guacamayo.registrarAnimal()
guacamayo.mostrarAnimal()


