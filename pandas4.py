import pandas as pd
df1 = pd.read_csv('surveys.csv')

df2 = df1['month'] #crea un subconjunto del dataframe
print(df2, type(df2))
df3 = df1[['species_id','plot_id']] #crea un subconjunto de varias columnas
print(df3, type(df3))
print(df1[50:61]) #filas de la 50 a la 60
print(df1)
print(df1.iloc[1]) # imprime la fil 1 de df1
print(df1.iloc[1,7]) # imprime la columna 7 de la fila 1, es decir un solo dato
print(df1.iloc[0:4,1:3])
print(df1.iloc[[0,3,9,10],:])
#filtros
print(df1[df1.year == 1985])
print(df1[(df1.year>=1985) & (df1.year<=1995) ]) # and:&, or:|, not:~