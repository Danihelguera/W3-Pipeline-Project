def leer_datos() :
    import pandas as pd
    import os
    df = pd.DataFrame()
    for ruta in os.listdir('data/accidents') :
        print(f"Leemos {'data/accidents/' + ruta} y adjuntamos en el dataframe")
        dfnew = pd.read_csv('data/accidents/' + ruta,encoding='latin-1')
        dfnew.rename(columns={'Numero_expedient'           : 'Expediente', 
                               'Codi_expedient'             : 'Expediente',
                               "Codi d'expedient"           : 'Expediente',

                               'Codi_districte'             : 'Distrito_codigo', 
                               'Codi districte'             : 'Distrito_codigo',                        

                               'Nom_districte'              : 'Distrito', 
                               'Nom districte'              : 'Distrito', 

                               'Codi_barri'                 : 'Barrio_codigo',
                               'Codi barri'                 : 'Barrio_codigo',

                               'Nom_barri'                  : 'Barrio',
                               'Nom barri'                  : 'Barrio',
                       
                               'Codi_carrer'                : 'Calle_codigo',
                               'Codi carrer'                : 'Calle_codigo',

                               'Nom_carrer'                 : 'Calle',
                               'Nom carrer'                 : 'Calle',

                               'Num_postal'                 : 'Codigo_Postal',
                               'Num_postal '                : 'Codigo_Postal',
                               'Num postal caption'         : 'Codigo_Postal',

                               'Descripcio_dia_setmana'     : 'Dia_semana', 
                               'Descripció dia setmana'     : 'Dia_semana', 
                               'Descripci¢ dia setmana'     : 'Dia_semana', 

                               'Dia_setmana'                : 'Dia_semana_corto', 
                               'Dia setmana'                : 'Dia_semana_corto', 

                               'Descripcio_tipus_dia'       : 'Tipo_dia',
                               'Descripció tipus dia'       : 'Tipo_dia',
                               'Descripci¢ tipus dia'       : 'Tipo_dia',

                               'NK_Any'                     : 'Año', 
                               'NK Any'                     : 'Año', 
                               'Any'                        : 'Año', 

                               'Mes_any'                    : 'Mes',
                               'Mes de any'                 : 'Mes',

                               'Nom_mes'                    : 'Mes_texto',  
                               'Nom mes'                    : 'Mes_texto',  

                               'Dia_mes'                    : 'Dia_mes' , 
                               'Dia de mes'                 : 'Dia_mes' , 

                               'Hora_dia'                   : 'Hora',
                               'Hora de dia'                : 'Hora',

                               'Descripcio_torn'            : 'Turno', 

                               'Descripcio_causa_vianant'   : 'Causa',
                               'Descripció causa vianant'   : 'Causa',
                               'Descripci¢ causa vianant'   : 'Causa',
                    
                               'Descripcio_tipus_vehicle'   : 'Tipo_vehiculo', 
                               'Descripció tipus de vehicle': 'Tipo_vehiculo', 
                               'Descripci¢ tipus de vehicle': 'Tipo_vehiculo', 

                               'Descripcio_model'           : 'Modelo', 
                               'Descripció model'           : 'Modelo', 
                               'Descripci¢ model'           : 'Modelo', 

                               'Descripcio_marca'           : 'Marca',
                               'Descripció marca'           : 'Marca',
                               'Descripci¢ marca'           : 'Marca',

                               'Descripcio_color'           : 'Color', 
                               'Descripció color'           : 'Color', 
                               'Descripci¢ color'           : 'Color', 

                               'Descripcio_carnet'          : 'Carnet', 
                               'Descripció carnet'          : 'Carnet', 
                               'Descripci¢ carnet'          : 'Carnet', 

                               'Antiguitat_carnet'          : 'Antiguedad',  
                               'Antiguitat carnet'          : 'Antiguedad',  

                               'Coordenada_UTM_X'           : 'Coordenada_UTM_X', 
                               'Coordenada UTM (X)'         : 'Coordenada_UTM_X', 

                               'Coordenada_UTM_Y'           : 'Coordenada_UTM_Y', 
                               'Coordenada UTM (Y)'	        : 'Coordenada_UTM_Y', 

                               'Latitud'                    : 'Latitud', 
                               ' Latitud'                   : 'Latitud', 
        
                               'Longitud'                   : 'Longitud',
                               ' Longitud'                  : 'Longitud',
        
                              }, inplace=True)
        df = pd.concat([df, dfnew], ignore_index=True)
    return df


def traducir_colores(df) :
    df.Color.fillna('Desconocido' , inplace = True)    
    df.Color.replace({  'Desconegut'   : 'Desconocido', 
                        'Negre'        : 'Negro', 
                        'Gris'         : 'Gris',
                        'Verd'         : 'Verde', 
                        'Vermell'      : 'Rojo', 
                        'Negre/Groc'   : 'Negro/Amarillo',
                        'Blanc'        : 'Blanco', 
                        'Altres'       : 'Desconocido', 
                        'Blau'         : 'Azul', 
                        'granate'      : 'Granate', 
                        'Groc'         : 'Amarillo', 
                        'Platejat'     : 'Plateado', 
                        'Taronja'      : 'Naranja', 
                        'Daurat'       : 'Dorado', 
                        'Marró'        : 'Marron',
                        'Marr¢'        : 'Marron', 
                        'MarrÃ³'       : 'Marron',
                        'Beige'        : 'Beige'
                    }, inplace = True)
    print("Se han traducido los colores a castellaño")
    return df
        
    


def traducir_dias_semana(df) :
    df.Dia_semana.replace({  
                            'Dilluns'   : 'Lunes', 
                            'Dimarts'   : 'Martes', 
                            'Dimecres'  : 'Miercoles', 
                            'Dijous'    : 'Jueves',  
                            'Divendres' : 'Viernes',
                            'Dissabte'  : 'Sabado', 
                            'Diumenge'  : 'Domingo'
                           }, inplace = True)
    df.Dia_semana_corto.replace({
                                  'Dl' : 'L', 
                                  'Dm' : 'M', 
                                  'Dc' : 'X', 
                                  'Dj' : 'J', 
                                  'Dv' : 'V', 
                                  'Ds' : 'S', 
                                  'Dg' : 'D'        
                                }, inplace = True)
    print("Se han traducido los dias de la semana a castellaño")
    return df

def traducir_meses(df) :
    df.Mes_texto.replace( {
                            'Gener'      : 'Enero', 
                            'Febrer'     : 'Febrero', 
                            'Mar\x87'    : 'Marzo', 
                            'Març'       : 'Marzo',
                            'MarÃ§'      : 'Marzo',
                            'Abril'      : 'Abril', 
                            'Maig'       : 'Mayo', 
                            'Juny'       : 'Junio', 
                            'Juliol'     : 'Julio',
                            'Agost'      : 'Agosto', 
                            'Setembre'   : 'Septiembre', 
                            'Octubre'    : 'Octubre', 
                            'Novembre'   : 'Noviembre', 
                            'Desembre'   : 'Diciembre'
                          }, inplace = True)
    print("Se han traducido los meses a castellaño")
    return df
    
    
def traducir_tipo_vehiculo(df) :
    df["Tipo_veh_grup"] = df.Tipo_vehiculo
    df.Tipo_veh_grup.replace({ 
                                'Bicicleta'                           : 'Bicicleta',
                                'Ciclomotor'                          : 'Ciclomotor',
                                'Cuadriciclo >=75cc'                  : 'Motocicleta',
                                'Cuadriciclo <75cc'                   : 'Motocicleta',
                                'Quadricicle > 75 cc'                 : 'Motocicleta',
                                'Quadricicle < 75 cc'                 : 'Motocicleta',
                                'Motocicleta'                         : 'Motocicleta',
                                'Carro'                               : 'Turismo',
                                'Turismo'                             : 'Turismo',
                                'Turisme'                             : 'Turismo',
                                'Taxi'                                : 'Turismo',
                                'Todo terreno'                        : 'Turismo',
                                'Tot terreny'                         : 'Turismo',
                                'Pick-up'                             : 'Turismo',
                                'Autocaravana'                        : 'Furgoneta',
                                'Furgoneta'                           : 'Furgoneta',
                                'AmbulÃ\xa0ncia'                      : 'Furgoneta',
                                'Cami¢n <= 3,5 Tm'                    : 'Camion',
                                'Cami¢n > 3,5 Tm'                     : 'Camion',
                                'Camión <= 3,5 Tm'                    : 'Camion',
                                'Camión > 3,5 Tm'                     : 'Camion',
                                'CamiÃ³n > 3,5 Tm'                    : 'Camion',
                                'CamiÃ³n <= 3,5 Tm'                   : 'Camion',
                                'CamiÃ³ rÃ\xadgid <= 3,5 tones'       : 'Camion',
                                'CamiÃ³ rÃ\xadgid > 3,5 tones'        : 'Camion',
                                'Tractocamión'                        : 'Camion',
                                'Tractocami¢n'                        : 'Camion',
                                'TractocamiÃ³n'                       : 'Camion',
                                'Tractor camiÃ³'                      : 'Camion',
                                'Autob£s'                             : 'Autobus',
                                'Autob£s articulado'                  : 'Autobus',
                                'Microbus <=17 plazas'                : 'Autobus',
                                'Microbus <= 17'                      : 'Autobus',  
                                'MicrobÃºs <= 17'                     : 'Autobus',   
                                'Autocar'                             : 'Autobus',
                                'Autobús'                             : 'Autobus',
                                'Autobús articulado'                  : 'Autobus',
                                'AutobÃºs'                            : 'Autobus',
                                'AutobÃºs articulado'                 : 'Autobus',
                                'AutobÃºs articulat'                  : 'Autobus',
                                'Veh. mobilitat personal amb motor'   : 'Otros',
                                'Veh. mobilitat personal sense motor' : 'Otros', 
                                'Otros veh¡c. a motor'                : 'Otros',
                                'Otros vehíc. a motor'                : 'Otros',
                                'Otros vehÃ\xadc. a motor'            : 'Otros',
                                'Altres vehicles sense motor'         : 'Otros',
                                'Altres vehicles amb motor'           : 'Otros',
                                "MaquinÃ\xa0ria d'obres i serveis"    : 'Otros',
                                'Maquinaria de obras'                 : 'Otros',
                                'Maquinaria agr¡cola'                 : 'Otros',
                                'Tranvía o tren'                      : 'Otros',
                                'TranvÃ\xada o tren'                  : 'Otros',
                                'Tren o tramvia'                      : 'Otros',
                                'Tranv¡a o tren'                      : 'Otros',
                                'Desconegut'                          : 'Desconocido'
                            },inplace=True)
    print("Se han clasificado los tipos de vehículos en castellaño")
    return df
                     
                     
def limpiar_Carnets(df) :
    df['Carnet_reducido']=df.Carnet
    df.Carnet_reducido.fillna('Desconocido')
    df.Carnet_reducido.replace( { 
                        'A'                : 'A',
                        'AM'               : 'A',
                        'A1'               : 'A',
                        'A2'               : 'A',
                        'B'                : 'B',
                        'B1'               : 'B',
                        'BTP'              : 'B',
                        'C1'               : 'C',
                        'C'                : 'C',
                        'D1'               : 'D',
                        'D'                : 'D',
                        'E B'              : 'E',
                        'E C1'             : 'E',
                        'E C'              : 'E', 
                        'E D'              : 'E', 
                        'E D1'             : 'E',  
                        'Desconegut'       : 'Desconocido',
                        'Llic\x8ancia'     : 'Licencia',
                        'Llicència'        : 'Licencia', 
                        'LlicÃ¨ncia'       : 'Licencia',
                        'Es desconeix'     : 'Desconocido',
                        'Sense permÃ\xads' : 'Sin permiso' 
                        },inplace=True)
    print("Se han clasificado los carnets")
    return df

def limpiar_antiguedad(df) :
    df.Antiguedad.fillna('Desconocido')
    df.Antiguedad.replace({
                            'Desconegut' : 'Desconocido',
                            '-2965'      : 'Desconocido', 
                            '-23'        : 'Desconocido', 
                            '-978'       : 'Desconocido',
                            '-2'         : 'Desconocido', 
                            '-54'        : 'Desconocido', 
                            '-77'        : 'Desconocido', 
                            '-196'       : 'Desconocido',
                            '-5'         : 'Desconocido', 
                            '-999'       : 'Desconocido',
                            '-7'         : 'Desconocido', 
                            '-3'         : 'Desconocido', 
                            '-195'       : 'Desconocido',
                            '-49'        : 'Desconocido', 
                            '-34'        : 'Desconocido', 
                            '-43'        : 'Desconocido',
                            '-194'       : 'Desconocido',
                            '-953'       : 'Desconocido',
                            '-2185'      : 'Desconocido',
                            '-969'       : 'Desconocido', 
                            '-48'        : 'Desconocido', 
                            '-4'         : 'Desconocido', 
                            '-70'        : 'Desconocido', 
                            '-947'       : 'Desconocido', 
                            '-41'        : 'Desconocido', 
                            '-47'        : 'Desconocido', 
                            '-45'        : 'Desconocido', 
                            '-28'        : 'Desconocido', 
                            '1018'       : 'Desconocido',
                            '-72'        : 'Desconocido', 
                            '1818'       : 'Desconocido',
                            '-46'        : 'Desconocido', 
                            '-484'       : 'Desconocido',
                            '-972'       : 'Desconocido',
                            '-189'       : 'Desconocido',
                            }, inplace = True)
    print("Se han limpiado las antiguedades incoherentes")
    return df
 
 
def limpiar_distrito(df) :
    df.Distrito.replace({  'Ciutat Vella'            : 'Ciutat Vella',
                            'Eixample'                : 'Eixample',
                            'Horta-Guinardó'          : 'Horta-Guinardó', 
                            'Horta-Guinard¢'          : 'Horta-Guinardó', 
                            'Horta-GuinardÃ³'         : 'Horta-Guinardó', 
                            'Gràcia'                  : 'Gràcia',  
                            'GrÃ\xa0cia'              : 'Gràcia',   
                            'Gr\x85cia'               : 'Gràcia', 
                            'Les Corts'               : 'Les Corts',
                            'Nou Barris'              : 'Nou Barris' , 
                            'Sant Andreu'             : 'Sant Andreu', 
                            'Sant Martí'              : 'Sant Martí', 
                            'Sant Mart¡'              : 'Sant Martí',  
                            'Sant MartÃ\xad'          : 'Sant Martí',  
                            'Sants-Montjuïc'          : 'Sants-Montjuïc',
                            'Sants-Montju\x8bc'       : 'Sants-Montjuïc', 
                            'Sants-MontjuÃ¯c'         : 'Sants-Montjuïc',
                            'Sarrià-Sant Gervasi'     : 'Sarrià-Sant Gervasi',
                            'Sarri\x85-Sant Gervasi'  : 'Sarrià-Sant Gervasi', 
                            'SarriÃ\xa0-Sant Gervasi' : 'Sarrià-Sant Gervasi',
                            'Desconegut'              : 'Desconocido' 
                            }, inplace = True)
    print("Se han corregido y unificado los nombres de los distritos")
    return df


def traducir_causa(df):
    df.Causa.replace({
                        'Creuar per fora pas de vianants'         : 'Cruzar por fuera paso de peatones', 
                        'No és causa del  vianant'                : 'No debido al peatón', 
                        'No \x82s causa del  vianant'             : 'No debido al peatón',
                        'No Ã©s causa del  vianant'               : 'No debido al peatón',     
                        'Altres'                                  : 'Otros', 
                        'Desobeir el senyal del sem\x85for'       : 'Desobedecer semáforo', 
                        'Desobeir el senyal del semàfor'          : 'Desobedecer semáforo',     
                        'Desobeir el senyal del semÃ\xa0for'      : 'Desobedecer semáforo',   
                        'Desobeir altres senyals'                 : 'Desobedecer señales', 
                        'Transitar a peu per la cal\x87ada'       : 'Transitar a pie por la calzada', 
                        'Transitar a peu per la calçada'          : 'Transitar a pie por la calzada', 
                        'Transitar a peu per la calÃ§ada'         : 'Transitar a pie por la calzada'
                    },inplace = True)   
    print("Se han traducido las causas del accidente a castellaño")
    return df
     
     
def turno_segun_hora(hora):
    if hora>22 or hora<6:
        return 'Noche'
    elif hora <13:
        return 'Mañana'
    else :
        return 'Tarde'

def calcular_turno(df) :
    df.Turno = df['Hora'].map(lambda x:turno_segun_hora(x))
    print('Se han calculado los turnos según la hora')
    return df
    