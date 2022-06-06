import pandas as pd
df1 = pd.read_csv('surveys.csv')
print(df1)
print(df1.head(20))
print(df1.tail(10))
print(df1.shape)
print(df1.columns)
print(pd.unique(df1['species_id'])) #devuelve una lista con los valores unicos de una columna
print(df1['species_id'].value_counts()) #Cuenta los valores únicos de una columna
print(df1['weight'].describe()) #Devuelve un análisis de esdística descriptiva
print(df1['weight'].mean()) #Devuelve el promedio de la columna
print(df1.groupby('species_id')['plot_id'].count()['BA'])



