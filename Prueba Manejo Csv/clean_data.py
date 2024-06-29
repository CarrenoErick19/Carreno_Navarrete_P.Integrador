# 3. Aquí colocarás el código para limpiar los datos, como se discutió anteriormente.

# clean_data.py

import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

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

def stem_tokens(tokens):
    stemmer = SnowballStemmer('spanish')
    tokens_stemizados = [stemmer.stem(token) for token in tokens]
    return tokens_stemizados

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
    
    # Tokenizar, eliminar stopwords y lematizar los comentarios
    df['comentarios'] = df['comentarios'].apply(tokenizar_texto)
    df['comentarios'] = df['comentarios'].apply(eliminar_stopwords)
    df['comentarios'] = df['comentarios'].apply(lematizar_tokens)  # Puedes usar lematización o stemming
    
    # Mostrar las primeras filas después de la limpieza y tokenización
    print(df.head())
