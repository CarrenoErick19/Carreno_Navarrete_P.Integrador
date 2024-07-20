import pandas as pd
from data.data_cleaning import limpiar_datos
from data.data_split import dividir_datos
from rnn_model.definir_modelo import definir_modelo
from rnn_model.entrenar_modelo import entrenar_modelo_rnn
from rnn_model.evaluar_modelo import evaluar_modelo
from rnn_model.guardar_modelo import guardar_modelo
from analysis.analisis_sentimiento import analizar_sentimientos
from analysis.identificacion_temas import identificar_temas
from analysis.comparacion import comparar_resultados
from analysis.visualization import mostrar_graficos

# Cargar datos
print("Cargando datos...")
data_path = 'datasets/datos_combinados_1.csv'
df = pd.read_csv(data_path)

# Limpiar datos
print("Limpiando datos...")
df = limpiar_datos(df)
print("Columnas disponibles después de limpiar los datos:", df.columns)

# Analizar sentimientos
print("Análisis de sentimientos...")
df, emociones = analizar_sentimientos(df)
print("Columnas disponibles después del análisis de sentimientos:", df.columns)

# Dividir datos en entrenamiento, validación y prueba
print("Dividiendo datos en entrenamiento, validación y prueba...")
train_df, val_df, test_df = dividir_datos(df)

# Verificar y limpiar datos para el modelo
def verificar_datos(df, columna):
    df = df.dropna(subset=[columna])  # Eliminar filas con valores nulos en la columna especificada
    df = df[df[columna].apply(lambda x: isinstance(x, str) and x.strip() != '')]  # Mantener solo valores válidos
    return df

train_df = verificar_datos(train_df, 'comment_limpio')
val_df = verificar_datos(val_df, 'comment_limpio')

# Definir y entrenar el modelo
print("Definiendo el modelo...")
model, tokenizer = definir_modelo(train_df)

print("Entrenando el modelo...")
model = entrenar_modelo_rnn(model, train_df, val_df, tokenizer, epochs=100)

# Guardar el modelo y el tokenizer
print("Guardando el modelo y el tokenizer...")
guardar_modelo(model, tokenizer, 'modelo_rnn.keras', 'tokenizer.pickle')

# Evaluar el modelo
print("Evaluando el modelo...")
evaluar_modelo(model, test_df, tokenizer)

# Identificar temas
print("Identificación de temas...")
df, temas = identificar_temas(df)

# Comparar resultados
print("Comparando resultados con datos anteriores...")
resultados_anteriores = comparar_resultados(df)

# Mostrar gráficos
print("Mostrando gráficos de estadísticas...")
mostrar_graficos(df, emociones, temas)

print("Ejecución completada.")
