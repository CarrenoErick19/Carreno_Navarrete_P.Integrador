import pandas as pd

def analizar_sentimientos(df):
    # Asegurarse de que la columna 'comment_limpio' está presente
    if 'comment_limpio' not in df.columns:
        raise ValueError("La columna 'comment_limpio' no está presente en el DataFrame.")
    
    emociones = {'satisfacción': [], 'insatisfacción': [], 'enojo': [], 'alegría': [], 'tristeza': []}
    df['aspecto'] = 'general'  # Asignar un valor por defecto a la columna 'aspecto'
    df['sentimiento'] = 0  # Crear columna 'sentimiento' y asignar valor por defecto
    
    for index, row in df.iterrows():
        texto = row['comment_limpio']
        if 'satisfacción' in texto:
            emociones['satisfacción'].append(texto)
            df.at[index, 'sentimiento'] = 1  # Ejemplo de asignación de sentimiento positivo
        elif 'insatisfacción' in texto:
            emociones['insatisfacción'].append(texto)
            df.at[index, 'sentimiento'] = -1  # Ejemplo de asignación de sentimiento negativo
        elif 'enojo' in texto:
            emociones['enojo'].append(texto)
            df.at[index, 'sentimiento'] = -1  # Ejemplo de asignación de sentimiento negativo
        elif 'alegría' in texto:
            emociones['alegría'].append(texto)
            df.at[index, 'sentimiento'] = 1  # Ejemplo de asignación de sentimiento positivo
        elif 'tristeza' in texto:
            emociones['tristeza'].append(texto)
            df.at[index, 'sentimiento'] = -1  # Ejemplo de asignación de sentimiento negativo
        
        # Asignar el aspecto basado en alguna lógica, por ejemplo, palabras clave
        if 'servicio' in texto:
            df.at[index, 'aspecto'] = 'servicio'
        elif 'precio' in texto:
            df.at[index, 'aspecto'] = 'precio'
        elif 'calidad' in texto:
            df.at[index, 'aspecto'] = 'calidad'
    
    return df, emociones
