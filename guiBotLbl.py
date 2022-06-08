#widgets, ejemplos botones, las etiquetas, los botones radiales
# Realice una gui que contenga dos botones y una etiqueta para realizar
# un contador ascendente y descendente

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.numero=0
        self.ventana1 = tk.Tk()
        self.ventana1.title('Contador')
        self.etiqueta1 = tk.Label(self.ventana1, text=self.numero, foreground="red")
        self.etiqueta1.grid(column=1, row=0)
        self.boton1 = tk.Button(self.ventana1, text='Incrementar', command=self.incrementar)
        self.boton1.grid(column=0, row=1)
        self.boton2 = tk.Button(self.ventana1, text='Decrementar', command=self.decrementar)
        self.boton2.grid(column=2, row=1)
        self.ventana1.mainloop()
    
    def incrementar(self):
        self.numero = self.numero + 1
        self.etiqueta1['text'] = self.numero
        #self.etiqueta1.confi(text=self.numero)
    
    def decrementar(self):
        self.numero = self.numero - 1
        self.etiqueta1['text'] = self.numero
        

aplicacion1 = Aplicacion()

