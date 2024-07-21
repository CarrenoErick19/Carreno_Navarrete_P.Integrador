import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generar_visualizaciones(df):
    # Mapeo de los sentimientos para etiquetas comprensibles
    sentimiento_map = {0: 'alegría', 1: 'enojo', 2: 'tristeza', 3: 'satisfacción', 4: 'insatisfacción'}
    df['sentimiento_label'] = df['sentimiento'].map(sentimiento_map)

    # Conteo de sentimientos
    plt.figure(figsize=(10, 6))
    sns.countplot(x='sentimiento_label', data=df, palette='viridis')
    plt.title('Distribución de Sentimientos')
    plt.xlabel('Sentimientos')
    plt.ylabel('Conteo')
    plt.show()

    # Evolución temporal de los sentimientos
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    plt.figure(figsize=(14, 7))
    df.resample('M', on='timestamp').size().plot(legend=False)
    plt.title('Número de Comentarios por Mes')
    plt.xlabel('Fecha')
    plt.ylabel('Número de Comentarios')
    plt.show()

    # Análisis de temas y aspectos
    if 'aspecto' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(x='aspecto', data=df, palette='coolwarm')
        plt.title('Distribución de Aspectos')
        plt.xlabel('Aspectos')
        plt.ylabel('Conteo')
        plt.show()

    # Si la columna 'emociones' no existe, no hacer nada más
    if 'emociones' not in df.columns:
        print("La columna 'emociones' no está presente en el DataFrame.")
        return

    # Analizar y visualizar las emociones
    emociones_df = pd.DataFrame(df['emociones'].tolist())
    emociones_df = emociones_df.apply(pd.Series.value_counts).fillna(0)

    plt.figure(figsize=(12, 6))
    emociones_df.plot(kind='bar', stacked=True)
    plt.title('Distribución de Emociones')
    plt.xlabel('Emociones')
    plt.ylabel('Conteo')
    plt.show()
