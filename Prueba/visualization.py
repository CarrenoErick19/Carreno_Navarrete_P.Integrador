# 3. Este archivo contendrá las funciones para la visualización de resultados.

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def plot_confusion_matrix(y_test, predictions):
    cm = confusion_matrix(y_test, predictions)
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

def plot_sentiment_distribution(df):
    plt.figure(figsize=(10, 7))
    sns.countplot(df['sentimiento'])
    plt.title('Distribución de Sentimientos')
    plt.xlabel('Sentimiento')
    plt.ylabel('Cantidad')
    plt.show()
