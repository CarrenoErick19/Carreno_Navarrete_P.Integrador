import pandas as pd
from data.data_cleaning import limpiar_datos
from data.data_split import dividir_datos
from analysis.analisis_sentimiento import analizar_sentimientos
from analysis.visualization import generar_visualizaciones
from rnn_model.definir_modelo import definir_modelo_rnn
from rnn_model.entrenar_modelo import entrenar_modelo_rnn
from rnn_model.evaluar_modelo import evaluar_modelo
import pickle

# Función para mostrar solo una pequeña parte del dataframe
def mostrar_muestra(df, n=10):
    print(df.head(n))

# Cargar datos
print("Cargando datos...")
df = pd.read_csv('datasets/datos_combinados_1.csv')
print(f"Datos cargados: {len(df)} registros, {len(df.columns)} columnas")
mostrar_muestra(df)  # Mostrar solo las primeras 10 líneas

# Limpiar datos
print("Limpiando datos...")
df = limpiar_datos(df)
print(f"Columnas disponibles después de limpiar los datos: {df.columns}")
mostrar_muestra(df)  # Mostrar una muestra de los datos limpiados

# Análisis de sentimientos
print("Análisis de sentimientos...")
df, emociones = analizar_sentimientos(df)
print(f"Columnas disponibles después del análisis de sentimientos: {df.columns}")
print(f"Emociones detectadas: {{'satisfacción': {len(emociones['satisfacción'])}, 'insatisfacción': {len(emociones['insatisfacción'])}, 'enojo': {len(emociones['enojo'])}, 'alegría': {len(emociones['alegría'])}, 'tristeza': {len(emociones['tristeza'])}}}")
mostrar_muestra(df)  # Mostrar una muestra de los datos después del análisis de sentimientos

# Dividir datos
print("Dividiendo datos en entrenamiento, validación y prueba...")
train_df, val_df, test_df = dividir_datos(df)
print(f"Datos de entrenamiento: {len(train_df)} registros")
print(f"Datos de validación: {len(val_df)} registros")
print(f"Datos de prueba: {len(test_df)} registros")
mostrar_muestra(train_df)  # Mostrar una muestra de los datos de entrenamiento

# Definir modelo
print("Definiendo el modelo...")
model, tokenizer = definir_modelo_rnn(vocab_size=5000, max_len=100)

# Entrenar modelo
print("Entrenando el modelo...")
model = entrenar_modelo_rnn(model, train_df, val_df, tokenizer, epochs=10)

# Guardar el modelo y el tokenizer
print("Guardando el modelo y el tokenizer...")
model.save('modelo_rnn.keras')
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle)
print("Modelo guardado en modelo_rnn.keras.")
print("Tokenizer guardado en tokenizer.pickle.")

# Evaluar modelo
print("Evaluando el modelo...")
metrics = evaluar_modelo(model, test_df, tokenizer)
print(f"Métricas del modelo - Accuracy: {metrics[0]}, Precision: {metrics[1]}, Recall: {metrics[2]}, F1 Score: {metrics[3]}")

# Generar visualizaciones
print("Generando visualizaciones...")
generar_visualizaciones(df)
print("Visualizaciones generadas.")
