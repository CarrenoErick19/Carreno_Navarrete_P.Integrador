# En este archivo, se encuentra el código para cargar 
# y mostrar los datos del archivo CSV.

import pandas as pd

def mostrar_datos_csv():
    # Cargar el CSV
    archivo_csv = r'C:\Users\PCarreño\Desktop\data_source\solca_comentarios.csv'
    df = pd.read_csv(archivo_csv, delimiter=';')
    
    # Mostrar las primeras filas por mediante el terminal para entender la estructura
    print(df.head())
    return df

