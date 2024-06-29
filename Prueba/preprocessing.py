# 1. Este archivo contendrá las funciones 
# relacionadas con la limpieza y preprocesamiento de datos.

import re
import string
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

# Descargar recursos de NLTK
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Configuración inicial
stop_words = set(stopwords.words('spanish'))
lemmatizer = WordNetLemmatizer()

def limpiar_texto(texto):
    texto = texto.lower()  # Convertir a minúsculas
    texto = re.sub(r'\d+', '', texto)  # Eliminar números
    texto = texto.translate(str.maketrans('', '', string.punctuation))  # Eliminar puntuación
    tokens = word_tokenize(texto)  # Tokenizar
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]  # Lematizar y eliminar stopwords
    return ' '.join(tokens)

def preprocess_data(input_file, output_file):
    try:
        df = pd.read_csv(input_file, quotechar='"', on_bad_lines='skip')
    except pd.errors.ParserError as e:
        print(f"Error al leer el archivo CSV: {e}")
        return

    # Asegurarse de que la columna de comentarios existe
    if 'comentarios' not in df.columns:
        print("Error: la columna 'comentarios' no se encuentra en el archivo CSV.")
        return

    # Limpiar la columna de comentarios
    df['texto_limpio'] = df['comentarios'].apply(limpiar_texto)
    
    # Guardar el archivo preprocesado
    df.to_csv(output_file, index=False)
