# crear una GUI, que contenga dos entry, para ingresar dos numeros y 
# 4 radio buttons para las cuatro operciones aritmética, un boton para operar
# y un label para el resultado
import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title('Calculadora')
        self.dato1 = tk.StringVar()
        self.entrada1 = tk.Entry(self.ventana1, width=20, textvariable=self.dato1)
        self.entrada1.grid(column= 0, row=0)
        self.dato2 = tk.StringVar()
        self.entrada2 = tk.Entry(self.ventana1, width=20, textvariable=self.dato2)
        self.entrada2.grid(column= 1, row=0)
        self.opcion = tk.IntVar()
        self.radio1 = tk.Radiobutton(self.ventana1, text = 'Suma', variable = self.opcion, value=1)
        self.radio1.grid(column= 0, row=1)
        self.radio2 = tk.Radiobutton(self.ventana1, text = 'Resta', variable = self.opcion, value=2)
        self.radio2.grid(column= 0, row=2)
        self.radio3 = tk.Radiobutton(self.ventana1, text = 'Multiplica', variable = self.opcion, value=3)
        self.radio3.grid(column= 0, row=3)
        self.radio4 = tk.Radiobutton(self.ventana1, text = 'Divide', variable = self.opcion, value=4)
        self.radio4.grid(column= 0, row=4)
        self.boton1 = tk.Button(self.ventana1, text = 'Operar', command = self.operaciones)
        self.boton1.grid(column= 0, row=5)
        self.etiqueta1 = tk.Label(self.ventana1, text='--')
        self.etiqueta1.grid(column= 0, row=6)
        self.ventana1.mainloop()
    
    def operaciones(self):
        if self.opcion.get()== 1:
            op = float(self.dato1.get())+float(self.dato2.get())
            self.etiqueta1.configure(text=op)
        elif self.opcion.get()==2:
            op = float(self.dato1.get())-float(self.dato2.get())
            self.etiqueta1.configure(text=op)
        elif self.opcion.get()==3:
            op = float(self.dato1.get())*float(self.dato2.get())
            self.etiqueta1.configure(text=op)
        else:
            op = float(self.dato1.get())/float(self.dato2.get())
            self.etiqueta1.configure(text=op)

aplicacion1 = Aplicacion()