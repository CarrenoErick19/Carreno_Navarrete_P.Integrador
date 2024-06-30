# 3. Aquí colocarás el código para limpiar los datos, como se discutió anteriormente.

# clean_data.py

import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from textblob import TextBlob

nltk.download('punkt')
nltk.download('stopwords')

def limpiar_caracteres(texto):
    if isinstance(texto, str):
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

def limpiar_datos():
    # Cargar el CSV
    archivo_csv = r'C:\Users\Erick Carreño\Desktop\data_source\solca_comentarios.csv'
    df = pd.read_csv(archivo_csv, delimiter=',')

    # Renombrar la columna 'comentario' a 'comentarios'
    df.rename(columns={'comentario': 'comentarios'}, inplace=True)
    
    # Aplicar limpieza y análisis de datos
    df['comentarios_limpios'] = df['comentarios'].apply(limpiar_caracteres)
    df['tokens'] = df['comentarios_limpios'].apply(tokenizar_texto)
    df['tokens'] = df['tokens'].apply(eliminar_stopwords)
    df['tokens'] = df['tokens'].apply(lematizar_tokens)
    
    # Generar la columna 'sentimiento'
    df['sentimiento'] = df['comentarios_limpios'].apply(lambda x: TextBlob(x).sentiment.polarity)
    
    # Mostrar las primeras líneas en una ventana gráfica (opcional)
    mostrar_datos_graficos(df)
    
    return df

def mostrar_datos_graficos(df):
    # Mostrar las primeras líneas en una ventana gráfica
    import tkinter as tk
    from tkinter import scrolledtext
    
    root = tk.Tk()
    root.title("Datos del CSV y Comentarios Limpios")
    
    # Mostrar primeras líneas del CSV original
    txt_original = scrolledtext.ScrolledText(root, width=80, height=5)
    txt_original.insert(tk.INSERT, "Comentarios originales:\n")
    txt_original.insert(tk.END, df['comentarios'].head().to_string(index=False))
    txt_original.pack()
    
    # Mostrar comentarios limpios
    txt_limpios = scrolledtext.ScrolledText(root, width=80, height=5)
    txt_limpios.insert(tk.INSERT, "\n\nComentarios después de la limpieza:\n")
    txt_limpios.insert(tk.END, df['tokens'].head().to_string(index=False))
    txt_limpios.pack()
    
    root.mainloop()
