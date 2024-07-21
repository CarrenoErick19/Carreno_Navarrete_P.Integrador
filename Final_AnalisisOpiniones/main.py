import pandas as pd
import tensorflow as tf
from tqdm import tqdm
import numpy as np
import pickle
from data.data_cleaning import limpiar_datos
from analysis.analisis_sentimiento import analizar_sentimientos
from rnn_model.definir_modelo import definir_modelo_rnn
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
df = df.dropna(subset=['sentimiento', 'comment_limpio'])

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

# Tokenizar los datos
tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=5000)  # Reducir el vocabulario a 5000 palabras
tokenizer.fit_on_texts(train_df['comment_limpio'].values)
X_train = tokenizer.texts_to_sequences(train_df['comment_limpio'].values)
X_val = tokenizer.texts_to_sequences(val_df['comment_limpio'].values)
X_test = tokenizer.texts_to_sequences(test_df['comment_limpio'].values)  # Tokenizar datos de prueba

# Padding
max_len = 50  # Reducir el maxlen a 50
X_train = tf.keras.preprocessing.sequence.pad_sequences(X_train, maxlen=max_len)
X_val = tf.keras.preprocessing.sequence.pad_sequences(X_val, maxlen=max_len)
X_test = tf.keras.preprocessing.sequence.pad_sequences(X_test, maxlen=max_len)  # Padding de datos de prueba

# Convertir etiquetas a numpy arrays
y_train = train_df['sentimiento'].values
y_val = val_df['sentimiento'].values
y_test = test_df['sentimiento'].values  # Etiquetas de prueba

# Definir el modelo con una red más simple
print("Definiendo el modelo...")
model = definir_modelo_rnn(vocab_size=5000, max_len=max_len)

# Implementar Early Stopping
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Entrenar el modelo con una barra de progreso
print("Entrenando el modelo...")
epochs = 100  # Se requieren 500 epochs
batch_size = 128  # Aumentado para mejorar la velocidad

with tqdm(total=epochs, desc="Training Model") as pbar:
    for epoch in range(epochs):
        history = model.fit(X_train, y_train, epochs=1, batch_size=batch_size, validation_data=(X_val, y_val), verbose=0)
        pbar.update(1)
        pbar.set_postfix(loss=history.history['loss'][-1], accuracy=history.history['accuracy'][-1], val_loss=history.history['val_loss'][-1], val_accuracy=history.history['val_accuracy'][-1])
        if early_stopping.stopped_epoch > 0:
            print(f"Early stopping at epoch {epoch+1}")
            break

# Guardar el modelo y el tokenizer
print("Guardando el modelo y el tokenizer...")
model.save('modelo_rnn.keras')
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle)
print("Modelo guardado en modelo_rnn.keras.")
print("Tokenizer guardado en tokenizer.pickle.")

# Evaluar el modelo
print("Evaluando el modelo...")
cr, cm = evaluar_modelo_rnn(model, test_df, tokenizer)

# Generar visualizaciones
print("Generando visualizaciones...")
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
generar_visualizaciones(df, y_test, y_pred_classes, ['alegría', 'enojo', 'tristeza', 'satisfacción', 'insatisfacción'])
print("Visualizaciones generadas.")
