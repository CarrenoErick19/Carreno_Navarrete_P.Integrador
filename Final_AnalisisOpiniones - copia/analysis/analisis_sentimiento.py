import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Inicializar el analizador de sentimientos de VADER
analyzer = SentimentIntensityAnalyzer()

# Diccionario de emociones para clasificar
sentimientos = {
    'alegría': 0, 
    'enojo': 1, 
    'tristeza': 2, 
    'satisfacción': 3, 
    'insatisfacción': 4
}

# Palabras clave y frases específicas del dialecto ecuatoriano para emociones negativas
palabras_clave_negativas = [
    'sinvergüenza', 'charlatán', 'mañoso', 'corrupto', 'inútil', 'maldito', 'ladrón', 'hipócrita',
    'vergonzoso', 'mentiroso', 'desgraciado', 'canalla', 'ratero'
]

# Función para clasificar el sentimiento basado en el análisis de VADER y palabras clave específicas
def clasificar_sentimiento(comentario):
    analisis = TextBlob(comentario)
    vader_result = analyzer.polarity_scores(comentario)
    
    # Clasificación basada en el análisis de VADER
    if vader_result['compound'] >= 0.5:
        return 'alegría'
    elif vader_result['compound'] >= 0.1:
        return 'satisfacción'
    elif vader_result['compound'] <= -0.5:
        return 'enojo'
    elif vader_result['compound'] <= -0.1:
        return 'tristeza'
    
    # Clasificación adicional basada en palabras clave específicas
    for palabra in palabras_clave_negativas:
        if palabra in comentario:
            return 'enojo'
    
    return 'insatisfacción'

def analizar_sentimientos(df):
    emociones = {'alegría': [], 'enojo': [], 'tristeza': [], 'satisfacción': [], 'insatisfacción': []}
    
    aspectos = []
    sentim = []

    for index, row in df.iterrows():
        comentario = row['comment_limpio']
        sentimiento = clasificar_sentimiento(comentario)
        emociones[sentimiento].append(comentario)
        aspectos.append('positivo' if sentimiento in ['alegría', 'satisfacción'] else 'negativo' if sentimiento in ['enojo', 'tristeza'] else 'neutral')
        sentim.append(sentimiento)
    
    df['aspecto'] = aspectos
    df['sentimiento'] = sentim
    df['sentimiento_label'] = df['sentimiento'].map(sentimientos)
    
    return df, emociones
