# 3. Aquí colocarás el código para limpiar los datos, como se discutió anteriormente.

# clean_data.py

import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from textblob import TextBlob  # Importar TextBlob para análisis de sentimientos

nltk.download('punkt')  # Descargar el tokenizer de NLTK
nltk.download('stopwords')  # Descargar la lista de stopwords de NLTK

def limpiar_caracteres(texto):
    if isinstance(texto, str):  # Verificar si es una cadena de texto
        texto_limpio = re.sub(r'[^a-zA-Z\s]', '', texto, flags=re.I|re.A)
        return texto_limpio.lower()
    else:
        return ''

def tokenizar_texto(texto):
    tokens = word_tokenize(texto)
    return tokens

def eliminar_stopwords(tokens):
    stopwords_esp = set(stopwords.words('spanish'))
    tokens_filtrados = [token for token in tokens if token.lower() not in stopwords_esp]
    return tokens_filtrados

def lematizar_tokens(tokens):
    lemmatizer = nltk.stem.WordNetLemmatizer()
    tokens_lemmatizados = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens_lemmatizados

def analizar_sentimiento(texto):
    sentimiento = TextBlob(texto).sentiment.polarity
    return sentimiento

def limpiar_datos():
    # Cargar el CSV
    archivo_csv = r'C:\Users\Erick Carreño\Desktop\data_source\comentarios_reddit.csv'
    df = pd.read_csv(archivo_csv, delimiter=';')
    
    # Eliminar comentarios duplicados
    df = df.drop_duplicates(subset=['comentarios'])
    
    # Manejar valores nulos o NaN en la columna 'comentarios'
    df['comentarios'] = df['comentarios'].fillna('')
    
    # Aplicar la limpieza a la columna 'comentarios'
    df['comentarios_limpios'] = df['comentarios'].apply(limpiar_caracteres)
    
    # Tokenizar, eliminar stopwords y lematizar los comentarios
    df['tokens'] = df['comentarios_limpios'].apply(tokenizar_texto)
    df['tokens'] = df['tokens'].apply(eliminar_stopwords)
    df['tokens'] = df['tokens'].apply(lematizar_tokens)
    
    # Realizar análisis de sentimientos
    df['sentimiento'] = df['tokens'].apply(lambda x: analizar_sentimiento(' '.join(x)))
    
    # Mostrar las primeras filas después de la limpieza y análisis de sentimientos
    print(df.head())
    
    return df  # Devolver el DataFrame limpio con análisis de sentimientos
