# 3. Aquí colocarás el código para limpiar los datos, como se discutió anteriormente.

# clean_data.py

import pandas as pd
import re

def limpiar_caracteres(texto):
    if isinstance(texto, str):  # Verificar si es una cadena de texto
        texto_limpio = re.sub(r'[^a-zA-Z\s]', '', texto, flags=re.I|re.A)
        return texto_limpio.lower()
    else:
        return ''

def limpiar_datos():
    # Cargar el CSV
    archivo_csv = r'C:\Users\Erick Carreño\Desktop\data_source\comentarios_reddit.csv'
    df = pd.read_csv(archivo_csv, delimiter=';')
    
    # Eliminar comentarios duplicados
    df = df.drop_duplicates(subset=['comentarios'])
    
    # Manejar valores nulos o NaN en la columna 'comentarios'
    df['comentarios'] = df['comentarios'].fillna('')
    
    # Aplicar la limpieza a la columna 'comentarios'
    df['comentarios'] = df['comentarios'].apply(limpiar_caracteres)
    
    # Mostrar las primeras filas después de la limpieza
    print(df.head())
