def cargar_datos_clima_api_aemet(fecha_inicio , fecha_final) :
    import os
    import json
    import pandas as pd
    import datetime
    import requests
    from dotenv import load_dotenv
    load_dotenv()
    
    aemet = os.getenv("aemet")
    parametros = {"api_key": aemet}

    url_A = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/"
    url_C = "T00%3A00%3A00UTC/fechafin/"
    url_E = "T23%3A59%3A59UTC/estacion/0201D"
    df_clima_BCN = pd.DataFrame()
    fecha_pivot = fecha_inicio

    while fecha_pivot <= fecha_final :
        
        fecha2 = fecha_pivot.replace(year=fecha_pivot.year+1)
        fecha2 = fecha2 - datetime.timedelta(days=1)
        
        url_B  = fecha_pivot.strftime("%Y-%m-%d")
        url_D  = fecha2.strftime("%Y-%m-%d")
        print(f"Leemos datos metereológicos de la API de AEMET desde {url_B} hasta {url_D}")
        res   = requests.get( url_A+url_B+url_C+url_D+url_E , params=parametros).json()
        datos = requests.get(res['datos']).json()
        datos_df = pd.DataFrame(datos)
        df_clima_BCN = pd.concat([df_clima_BCN , datos_df] , ignore_index=True )
        fecha_pivot = fecha2 + datetime.timedelta(days=1)
    
    print(f"Limitamos los datos meterológicos hasta la fecha_final {fecha_final}")
    df_clima_BCN = df_clima_BCN[df_clima_BCN.fecha <= fecha_final.strftime("%Y-%m-%d")]
    return df_clima_BCN




