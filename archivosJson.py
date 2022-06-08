import pandas as pd 
import json
#lectura de una archivo json con pandas
df = pd.read_json('ejemplo.json')
print(df)

#Conversion de un diccionario a json
diccionario ={
    "nombre":"Juan",
    "edad": 25,
    "profesion": "contador",
    "hijos": ['Ana', 'Julián'],
    "mascotas": None,
    "divorciado": False    
}
x = json.dumps(diccionario, indent=4, separators=(',', '='), ensure_ascii=False)
print(x)
print(type(x))

dicString = '{"nombre":"Juan","edad": 25,"profesion": "contador"}'
y = json.loads(dicString)
print(y, type(y))