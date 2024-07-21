import pandas as pd
from textblob import TextBlob

def analizar_sentimientos(df):
    sentimientos = {'alegría': 0, 'enojo': 1, 'tristeza': 2, 'satisfacción': 3, 'insatisfacción': 4}
    emociones = {'alegría': [], 'enojo': [], 'tristeza': [], 'satisfacción': [], 'insatisfacción': []}

    aspectos = []
    sentim = []

    for index, row in df.iterrows():
        comentario = row['comment_limpio']
        analisis = TextBlob(comentario)

        if analisis.sentiment.polarity > 0.5:
            emociones['alegría'].append(comentario)
            aspectos.append('positivo')
            sentim.append('alegría')
        elif analisis.sentiment.polarity > 0.1:
            emociones['satisfacción'].append(comentario)
            aspectos.append('positivo')
            sentim.append('satisfacción')
        elif analisis.sentiment.polarity < -0.5:
            emociones['enojo'].append(comentario)
            aspectos.append('negativo')
            sentim.append('enojo')
        elif analisis.sentiment.polarity < -0.1:
            emociones['tristeza'].append(comentario)
            aspectos.append('negativo')
            sentim.append('tristeza')
        else:
            emociones['insatisfacción'].append(comentario)
            aspectos.append('neutral')
            sentim.append('insatisfacción')

    df['aspecto'] = aspectos
    df['sentimiento'] = sentim

    df['sentimiento'] = df['sentimiento'].map(sentimientos)

    if not any(emociones.values()):
        raise ValueError("No se encontraron comentarios con emociones reconocidas.")
    
    return df, emociones
