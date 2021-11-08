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

df.drop(['Codigo_Postal', 'Turno', 'Tipo_dia', 'Longitud', 'Latitud'], axis=1, inplace=True)
print('Se han quitado columnas que no se usarán posteriormente')

df.Modelo.fillna('Desconocido',inplace = True)
df.Modelo.replace({'Desconegut':'Desconocido'})
df.Marca.fillna('Desconocido',inplace=True)
df.Marca.replace({'Desconegut':'Desconocido'})
df.Calle.fillna('Desconocido',inplace=True)
print('Se han limpiado los Nan y se han traducido los desconocidos a castellaño ')

df.to_csv('output/accidents_Bcn_limpio.csv' , index=False , encoding='latin-1')
print('Se ha exportado el un CSV con los datos limpios al directorio /output')