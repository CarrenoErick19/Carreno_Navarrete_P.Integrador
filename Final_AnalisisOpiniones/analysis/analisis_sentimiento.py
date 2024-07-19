from textblob import TextBlob

def analizar_sentimientos(df):
    emociones = {
        'satisfaccion': [],
        'insatisfaccion': [],
        'enojo': [],
        'alegria': [],
        'tristeza': []
    }

    for comentario in df['comentarios_limpios']:
        blob = TextBlob(comentario)
        sentimiento = blob.sentiment.polarity
        
        if sentimiento > 0.5:
            emociones['alegria'].append(comentario)
        elif sentimiento > 0.1:
            emociones['satisfaccion'].append(comentario)
        elif sentimiento < -0.5:
            emociones['enojo'].append(comentario)
        elif sentimiento < -0.1:
            emociones['tristeza'].append(comentario)
        else:
            emociones['insatisfaccion'].append(comentario)
    
    return emociones
