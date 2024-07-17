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

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

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

def cargar_csv(file_name):
    csv_path = os.path.join('datasets', file_name)
    df = pd.read_csv(csv_path, delimiter=',')
    df.rename(columns={'comentario': 'comentarios'}, inplace=True)
    return df

def limpiar_datos(df):
    # Aplicar limpieza de datos
    df['comentarios_limpios'] = df['comentarios'].apply(limpiar_caracteres)
    df['tokens'] = df['comentarios_limpios'].apply(tokenizar_texto)
    df['tokens'] = df['tokens'].apply(eliminar_stopwords)
    df['tokens'] = df['tokens'].apply(lematizar_tokens)
    
    return df

def vectorizar_texto(df):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['comentarios_limpios'])
    return tfidf_matrix, tfidf_vectorizer.get_feature_names_out()

def mostrar_resultados(df, tfidf_matrix, feature_names):
    root = tk.Tk()
    root.title("Resultados de Limpieza de Datos")

    tree = ttk.Treeview(root)
    tree["columns"] = ("comentarios", "comentarios_limpios", "tokens", "tfidf")

    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("comentarios", anchor=tk.W, width=200)
    tree.column("comentarios_limpios", anchor=tk.W, width=200)
    tree.column("tokens", anchor=tk.W, width=200)
    tree.column("tfidf", anchor=tk.W, width=200)

    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("comentarios", text="Comentarios Originales", anchor=tk.W)
    tree.heading("comentarios_limpios", text="Comentarios Limpios", anchor=tk.W)
    tree.heading("tokens", text="Tokens", anchor=tk.W)
    tree.heading("tfidf", text="TF-IDF", anchor=tk.W)

    for index, row in df.iterrows():
        tfidf_vector = tfidf_matrix[index].toarray().flatten()
        tfidf_scores = {feature_names[i]: tfidf_vector[i] for i in range(len(feature_names)) if tfidf_vector[i] > 0}
        tree.insert("", index, text="", values=(row["comentarios"], row["comentarios_limpios"], row["tokens"], str(tfidf_scores)))

    tree.pack(expand=True, fill='both')
    
    root.mainloop()

