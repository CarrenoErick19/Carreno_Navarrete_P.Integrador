import matplotlib.pyplot as plt
import pandas as pd

def mostrar_graficos(df, emociones, temas):
    # Conteo de sentimientos por aspecto
    aspectos = df['aspecto'].unique()
    conteo_sentimientos = {
        'negative': df[df['sentimiento'] == 'negative']['aspecto'].value_counts(),
        'neutral': df[df['sentimiento'] == 'neutral']['aspecto'].value_counts(),
        'positive': df[df['sentimiento'] == 'positive']['aspecto'].value_counts()
    }
    
    # Crear gráfico de barras para conteo de sentimientos por aspecto
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    ax1, ax2, ax3, ax4 = axes.flatten()

    ax1.bar(aspectos, conteo_sentimientos['negative'], label='Negative', color='red')
    ax1.bar(aspectos, conteo_sentimientos['neutral'], label='Neutral', color='grey', bottom=conteo_sentimientos['negative'])
    ax1.bar(aspectos, conteo_sentimientos['positive'], label='Positive', color='green', bottom=conteo_sentimientos['negative'] + conteo_sentimientos['neutral'])
    ax1.set_title('Sentiment Counts by Aspect')
    ax1.set_xlabel('Aspect')
    ax1.set_ylabel('Count')
    ax1.legend()

    # Crear gráfico de burbujas para conteo total por aspecto
    conteo_aspectos = df['aspecto'].value_counts()
    sizes = conteo_aspectos * 100
    ax2.scatter(conteo_aspectos.index, conteo_aspectos.values, s=sizes, alpha=0.5)
    for i, txt in enumerate(conteo_aspectos.index):
        ax2.annotate(txt, (conteo_aspectos.index[i], conteo_aspectos.values[i]))
    ax2.set_title('Counts by Aspect')
    ax2.set_xlabel('Aspect')
    ax2.set_ylabel('Count')

    # Crear gráfico de dispersión para menciones positivas vs negativas por aspecto
    positivos = df[df['sentimiento'] == 'positive']['aspecto'].value_counts()
    negativos = df[df['sentimiento'] == 'negative']['aspecto'].value_counts()
    ax3.scatter(negativos, positivos)
    for i, aspecto in enumerate(positivos.index):
        ax3.annotate(aspecto, (negativos[i], positivos[i]))
    ax3.set_title('Positive VS Negative mentions per aspect')
    ax3.set_xlabel('Negative mentions')
    ax3.set_ylabel('Positive mentions')

    # Gráfico de pastel para la distribución de emociones
    labels = emociones.keys()
    sizes = [len(emociones[emoción]) for emoción in emociones]
    ax4.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax4.axis('equal')
    ax4.set_title('Distribution of Emotions')

    plt.tight_layout()
    plt.show()
