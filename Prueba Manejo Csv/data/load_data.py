# 2. En este archivo, colocarás el código para cargar 
# y mostrar los datos del archivo CSV.

import pandas as pd

def mostrar_datos_csv():
    # Cargar el CSV
    archivo_csv = r'C:\Users\Erick Carreño\Desktop\data_source\solca_comentarios.csv'
    df = pd.read_csv(archivo_csv, delimiter=';')
    
    # Mostrar las primeras filas para entender la estructura
    print(df.head())
    return df

