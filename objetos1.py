# Programación Orientada a Objetos POO
# Python es un leguaje orientado a objetos
# Casi todo en Pythos es un objeto
# Una clase es un modelo o patrón del cual se pueden crear múltiples objetos
# En una clase se definen propiedades o atributos (variables) y métodos (funciones)
# Hay que declarar o crear una clase antes de poder crear objetos de esa clase
# Al crear un objeto de una clase, es lo mismo que decir: "crear una instancia de 
# una clase"

# Crear una clase e Python
class Persona:
    def crear(self, nombre:str):
        self.name = nombre
    
    def mostrar(self):
        print(self.name)

# crear una instacia de la clase persona (crear un objeto)
persona1 = Persona()
print(type(persona1))
persona1.crear('Juan')
persona1.mostrar()
persona2 = Persona()
persona2.crear('Ana')
persona2.mostrar()

# método epecial __init__, su principal objetivo es inicializar propiedades del
# objeto que se instancia
# El método __init__ se ejecuta cuando se crea el objeto, de forma automática
# El método __init__ no retorna datos
# Este método recibe parámetros para inicializar atributos o propiedades del objeto 

class Estudiante:
    def __init__(self):
        self.nombre = input('Ingrese el nombre del estudiante:\n')
        self.nota = float(input('Digite la nota del estudiante:\n'))
    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)
    def aprobar(self):
        if self.nota>=3:
            print('Aprobó')
        else:
            print('No aprobó')

a = Estudiante() #instaciar la clase Estudiante

a.nota = 3.5 #Modificar atributos
a.imprimir()
a.aprobar()
        
        
    



