# Realice una GUI, que reciba un numero entero por un Entry, y arroje el cuadrado 
# del número en una etiqueta, cuando se presione un boton

import tkinter as tk
from turtle import width

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title('Cuadrado')
        self.etiqueta1 = tk.Label(self.ventana1,text='Ingese un número entero')
        self.etiqueta1.grid(column=1, row=1)
        self.dato = tk.StringVar()
        self.entrada1 = tk.Entry(self.ventana1, width=10, textvariable=self.dato)
        self.entrada1.grid(column=1, row=2)
        self.boton1 = tk.Button(self.ventana1, text='Cuadrado', command=self.cuadrado)
        self.boton1.grid(column=1, row=3)
        self.etiqueta2 = tk.Label(self.ventana1, text='')
        self.etiqueta2.grid(column=1, row=4)
        self.ventana1.mainloop()
    
    def cuadrado(self):
        numero = float(self.dato.get())
        cuadrado= numero**2
        self.etiqueta2['text'] = cuadrado
        

aplicacion1 = Aplicacion()
