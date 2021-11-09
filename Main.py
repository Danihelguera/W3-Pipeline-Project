import json
import requests
import pandas as pd
from pandas import json_normalize
import os
from dotenv import load_dotenv
import datetime
import re

load_dotenv()

from src import cleaning_functions as cf

df = cf.leer_datos()
df = df[df.Expediente.isna()       == False]
df = df[df.Coordenada_UTM_Y.isna() == False]

cf.traducir_colores(df)
cf.traducir_dias_semana(df)
cf.traducir_meses(df)
cf.traducir_tipo_vehiculo(df)
cf.limpiar_Carnets(df)
cf.limpiar_antiguedad(df)
cf.limpiar_distrito(df)
cf.traducir_causa(df)
cf.calcular_turno(df)

df.drop(['Codigo_Postal', 'Tipo_dia', 'Longitud', 'Latitud'], axis=1, inplace=True)
print('Se han quitado columnas que no se usarán posteriormente')

df.Modelo.fillna('Desconocido',inplace = True)
df.Modelo.replace({'Desconegut':'Desconocido'})
df.Marca.fillna('Desconocido',inplace=True)
df.Marca.replace({'Desconegut':'Desconocido'})
df.Calle.fillna('Desconocido',inplace=True)
print('Se han limpiado los Nan y se han traducido los desconocidos a castellaño ')

df.to_csv('output/accidents_Bcn_limpio.csv' , index=False , encoding='latin-1')
print('\n')
print("Se ha exportado el archvo 'accidents_Bcn_limpio.csv' con los datos de accidentes limpios al directorio /output")
print('\n')

from datetime import date

fecha_1 = date(2010,  1,  1)
fecha_2 = date(2020, 12, 31)

print(f"Se consulta la API de AEMET para obtener datos metereológicos desde {fecha_1} hasta {fecha_2}")
from src import api_functions as af
df_clima_BCN = af.cargar_datos_clima_api_aemet(fecha_1 , fecha_2)

df_clima_BCN.to_csv('output/clima_BCN.csv' , index=False)
print('\n')
print("Se ha exportado el archivo 'clima_BCN.cse' con los datos metereológicos al directorio /output")
print('\n')
