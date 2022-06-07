# implemente una clase llamada Operaciones, se deben cargar dos valores
# decimales en el métod __init__ y calcular suma, resta, multiplicación 
# y división cada uno con un método

class Operaciones:
    def __init__(self, a:float, b:float) -> None:
        self.a = a
        self.b = b  
        
    def sum(self):
        print(f'La suma es: {self.a + self.b}') 
    
    def sub(self):
        print(f'La resta es: {self.a - self.b}')
        
    def mul(self):
        print(f'La multiplicación es: {self.a * self.b}')
        
    def div(self):
        try:
            print(f'La división es: {self.a / self.b}')
        except:
            print(f'Operación inválida')

a = Operaciones(8,0)
a.sum()
a.sub()
a.mul()
a.div()