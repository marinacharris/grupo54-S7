import pandas as pd
cadena = 'www.ejemplo.com'
#split
lista = cadena.split('.')
print(lista[-1])
rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true' 
try: 
    df1 = pd.read_csv(rutaFileCsv)
except:
    print('error en el archivo')
    
def saludo(a):
    b= 'Marina'
    print(a,b)
saludo('Hola')
