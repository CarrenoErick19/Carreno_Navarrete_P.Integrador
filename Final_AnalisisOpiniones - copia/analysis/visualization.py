import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generar_visualizaciones_completas(df, y_test, y_pred_classes, etiquetas, cm):
    # Mapeo de los sentimientos para etiquetas comprensibles
    sentimiento_map = {0: 'alegría', 1: 'enojo', 2: 'tristeza', 3: 'satisfacción', 4: 'insatisfacción'}
    df['sentimiento_label'] = df['sentimiento'].map(sentimiento_map)

    # Crear figura con subplots
    fig, axes = plt.subplots(2, 3, figsize=(20, 10))
    fig.suptitle('Análisis de Sentimientos y Aspectos', fontsize=16)

    # Conteo de sentimientos
    sns.countplot(x='sentimiento_label', data=df, palette='viridis', ax=axes[0, 0])
    axes[0, 0].set_title('Distribución de Sentimientos')
    axes[0, 0].set_xlabel('Sentimientos')
    axes[0, 0].set_ylabel('Conteo')

    # Evolución temporal de los sentimientos
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.resample('M', on='timestamp').size().plot(ax=axes[0, 1])
    axes[0, 1].set_title('Número de Comentarios por Mes')
    axes[0, 1].set_xlabel('Fecha')
    axes[0, 1].set_ylabel('Número de Comentarios')

    # Análisis de temas y aspectos
    if 'aspecto' in df.columns:
        sns.countplot(x='aspecto', data=df, palette='coolwarm', ax=axes[1, 0])
        axes[1, 0].set_title('Distribución de Aspectos')
        axes[1, 0].set_xlabel('Aspectos')
        axes[1, 0].set_ylabel('Conteo')

    # Nuevo gráfico de distribución de opiniones por año
    df['year'] = df['timestamp'].dt.year
    df_year_sentiment = df.groupby(['year', 'sentimiento_label']).size().unstack().fillna(0)
    df_year_sentiment.plot(kind='bar', stacked=True, ax=axes[1, 1])
    axes[1, 1].set_title('Distribución de Opiniones por Año')
    axes[1, 1].set_xlabel('Año')
    axes[1, 1].set_ylabel('Conteo')

    # Matriz de confusión
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=etiquetas, yticklabels=etiquetas, ax=axes[1, 2])
    axes[1, 2].set_title('Confusion Matrix')
    axes[1, 2].set_xlabel('Predicted')
    axes[1, 2].set_ylabel('True')

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

def generar_visualizaciones(df, y_test, y_pred_classes, etiquetas):
    # Mapeo de los sentimientos para etiquetas comprensibles
    sentimiento_map = {0: 'alegría', 1: 'enojo', 2: 'tristeza', 3: 'satisfacción', 4: 'insatisfacción'}
    df['sentimiento_label'] = df['sentimiento'].map(sentimiento_map)

    # Crear figura con subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Análisis de Sentimientos y Aspectos', fontsize=16)

    # Conteo de sentimientos
    sns.countplot(x='sentimiento_label', data=df, palette='viridis', ax=axes[0, 0])
    axes[0, 0].set_title('Distribución de Sentimientos')
    axes[0, 0].set_xlabel('Sentimientos')
    axes[0, 0].set_ylabel('Conteo')

    # Evolución temporal de los sentimientos
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.resample('M', on='timestamp').size().plot(ax=axes[0, 1])
    axes[0, 1].set_title('Número de Comentarios por Mes')
    axes[0, 1].set_xlabel('Fecha')
    axes[0, 1].set_ylabel('Número de Comentarios')

    # Análisis de temas y aspectos
    if 'aspecto' in df.columns:
        sns.countplot(x='aspecto', data=df, palette='coolwarm', ax=axes[1, 0])
        axes[1, 0].set_title('Distribución de Aspectos')
        axes[1, 0].set_xlabel('Aspectos')
        axes[1, 0].set_ylabel('Conteo')

    # Análisis de emociones (si existe)
    if 'emociones' in df.columns:
        emociones_df = pd.DataFrame(df['emociones'].tolist())
        emociones_df = emociones_df.apply(pd.Series.value_counts).fillna(0)
        emociones_df.plot(kind='bar', stacked=True, ax=axes[1, 1])
        axes[1, 1].set_title('Distribución de Emociones')
        axes[1, 1].set_xlabel('Emociones')
        axes[1, 1].set_ylabel('Conteo')
    else:
        axes[1, 1].axis('off')
        axes[1, 1].text(0.5, 0.5, 'La columna "emociones" no está presente en el DataFrame.', ha='center', va='center', fontsize=12)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
