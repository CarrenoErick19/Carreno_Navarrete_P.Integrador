import pandas as pd
import numpy as np
import pickle
import tensorflow as tf
from data.data_cleaning import limpiar_datos
from analysis.analisis_sentimiento import analizar_sentimientos
from rnn_model.definir_modelo import definir_modelo_rnn
from rnn_model.entrenar_modelo import entrenar_modelo_rnn
from rnn_model.evaluar_modelo import evaluar_modelo_rnn
from analysis.visualization import generar_visualizaciones

# Cargar datos
print("Cargando datos...")
df = pd.read_csv('datasets/datos_combinados_1.csv')
print(f"Datos cargados: {len(df)} registros, {len(df.columns)} columnas")
print(df.head(10))

# Limpiar datos
print("Limpiando datos...")
df = limpiar_datos(df)
print(f"Columnas disponibles después de limpiar los datos: {df.columns}")
print(df.head(10))

# Análisis de sentimientos
print("Análisis de sentimientos...")
df, emociones = analizar_sentimientos(df)
print(f"Columnas disponibles después del análisis de sentimientos: {df.columns}")
print(f"Emociones detectadas: { {key: len(value) for key, value in emociones.items()} }")
print(df.head(10))

# Verificar contenido de 'sentimiento_label'
print("Contenido de 'sentimiento_label':")
print(df['sentimiento_label'].unique())

# Corregir mapeo: asegurar que 'sentimiento_label' contenga cadenas
sentimiento_map = {'alegría': 0, 'enojo': 1, 'tristeza': 2, 'satisfacción': 3, 'insatisfacción': 4}
label_to_text = {v: k for k, v in sentimiento_map.items()}
df['sentimiento_label'] = df['sentimiento_label'].map(label_to_text)

# Convertir las etiquetas de sentimiento a valores numéricos
df['sentimiento'] = df['sentimiento_label'].map(sentimiento_map)

# Verificar mapeo
print("Verificación del mapeo de 'sentimiento_label' a 'sentimiento':")
print(df[['sentimiento_label', 'sentimiento']].drop_duplicates())

# Verificar valores NaN antes de eliminar
print(f"Valores NaN en 'sentimiento': {df['sentimiento'].isna().sum()}")

# Manejar valores NaN
df = df.dropna(subset=['sentimiento'])

# Verificar DataFrame después de eliminar valores NaN
print(f"Datos después de eliminar NaN en 'sentimiento': {len(df)} registros")
print(df.head(10))

# Dividir datos en entrenamiento, validación y prueba
print("Dividiendo datos en entrenamiento, validación y prueba...")
train_df, val_df, test_df = np.split(df.sample(frac=1, random_state=42), [int(.7*len(df)), int(.8*len(df))])
print(f"Datos de entrenamiento: {len(train_df)} registros")
print(f"Datos de validación: {len(val_df)} registros")
print(f"Datos de prueba: {len(test_df)} registros")
print(train_df.head(10))

# Verificar datos de entrenamiento
if len(train_df) == 0:
    raise ValueError("Datos de entrenamiento están vacíos.")

# Definir el modelo
print("Definiendo el modelo...")
model, tokenizer = definir_modelo_rnn(vocab_size=5000, max_len=100)

# Entrenar el modelo
print("Entrenando el modelo...")
model, tokenizer = entrenar_modelo_rnn(model, train_df, val_df, tokenizer, epochs=10)

# Guardar el modelo y el tokenizer
print("Guardando el modelo y el tokenizer...")
model.save('modelo_rnn.keras')
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle)
print("Modelo guardado en modelo_rnn.keras.")
print("Tokenizer guardado en tokenizer.pickle.")

# Evaluar el modelo
print("Evaluando el modelo...")
evaluar_modelo_rnn(model, test_df, tokenizer)

# Generar visualizaciones
print("Generando visualizaciones...")
generar_visualizaciones(df)
print("Visualizaciones generadas.")
