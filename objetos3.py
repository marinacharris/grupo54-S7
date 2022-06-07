# herencia 
# se puede definir una clase que hereda propiedades y métodos de otra clase
# Clase padre, clase pricipal, clase base, esta es la clase de la que se hereda
# Clase hija, clase secundaria, clase derivada, esta es la clase que hereda 

class Persona: # clase padre
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def imprimir(self):
        print(self.nombre, self.apellido)

x = Persona('Carlos','Arrieta')
x.imprimir()

class Estudiante(Persona): #clase hija
    def saludo(self):
        print(f'Hola {self.nombre} {self.apellido}, Bienvenido!')

y = Estudiante('Andrés', 'Guerrero')
y.imprimir()
y.saludo()

    
