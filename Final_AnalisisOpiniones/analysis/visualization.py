import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report

def generar_matriz_confusion(y_true, y_pred, labels, ax):
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels, ax=ax)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('True')
    ax.set_title('Confusion Matrix')

def generar_visualizaciones(df, y_true, y_pred, labels):
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

    # Matriz de confusión
    generar_matriz_confusion(y_true, y_pred, labels, axes[1, 1])

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
