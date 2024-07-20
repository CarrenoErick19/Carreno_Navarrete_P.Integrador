import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
import os
import tkinter as tk
from tkinter import ttk
from sklearn.feature_extraction.text import TfidfVectorizer

# Descargar y cargar manualmente los recursos necesarios de NLTK si no se han descargado previamente
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

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
    lemmatizer = WordNetLemmatizer()
    tokens_lemmatizados = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens_lemmatizados

def limpiar_datos_fila(fila):
    fila['comment_limpio'] = limpiar_caracteres(fila['comment'])
    tokens = tokenizar_texto(fila['comment_limpio'])
    tokens = eliminar_stopwords(tokens)
    tokens = lematizar_tokens(tokens)
    fila['tokens'] = tokens
    return fila

def cargar_csv(file_name):
    csv_path = os.path.join('datasets', file_name)
    df = pd.read_csv(csv_path, delimiter=',')
    df.rename(columns={'comment': 'comment'}, inplace=True)  # Asegurarse de que la columna se llama 'comment'
    return df

def limpiar_datos(df):
    filas_limpias = []
    for _, fila in df.iterrows():
        filas_limpias.append(limpiar_datos_fila(fila))
    df_limpio = pd.DataFrame(filas_limpias)
    return df_limpio

def vectorizar_texto(df):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['comment_limpio'])
    return tfidf_matrix, tfidf_vectorizer.get_feature_names_out()

def mostrar_resultados(df, tfidf_matrix, feature_names):
    root = tk.Tk()
    root.title("Resultados de Limpieza de Datos")

    tree = ttk.Treeview(root)
    tree["columns"] = ("comment", "comment_limpio", "tokens", "tfidf")

    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("comment", anchor=tk.W, width=200)
    tree.column("comment_limpio", anchor=tk.W, width=200)
    tree.column("tokens", anchor=tk.W, width=200)
    tree.column("tfidf", anchor=tk.W, width=200)

    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("comment", text="Comentarios Originales", anchor=tk.W)
    tree.heading("comment_limpio", text="Comentarios Limpios", anchor=tk.W)
    tree.heading("tokens", text="Tokens", anchor=tk.W)
    tree.heading("tfidf", text="TF-IDF", anchor=tk.W)

    for index, row in df.iterrows():
        tfidf_vector = tfidf_matrix[index].toarray().flatten()
        tfidf_scores = {feature_names[i]: tfidf_vector[i] for i in range(len(feature_names)) if tfidf_vector[i] > 0}
        tree.insert("", index, text="", values=(row["comment"], row["comment_limpio"], row["tokens"], str(tfidf_scores)))

    tree.pack(expand=True, fill='both')
    
    root.mainloop()
