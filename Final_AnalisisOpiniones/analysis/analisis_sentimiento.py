import pandas as pd

def analizar_sentimientos(df):
    # Asegurarse de que la columna 'comment_limpio' está presente
    if 'comment_limpio' not in df.columns:
        raise ValueError("La columna 'comment_limpio' no está presente en el DataFrame.")
    
    emociones = {'satisfacción': [], 'insatisfacción': [], 'enojo': [], 'alegría': [], 'tristeza': []}
    for index, row in df.iterrows():
        texto = row['comment_limpio']
        if 'satisfacción' in texto:
            emociones['satisfacción'].append(texto)
        elif 'insatisfacción' in texto:
            emociones['insatisfacción'].append(texto)
        elif 'enojo' in texto:
            emociones['enojo'].append(texto)
        elif 'alegría' in texto:
            emociones['alegría'].append(texto)
        elif 'tristeza' in texto:
            emociones['tristeza'].append(texto)
    return emociones
