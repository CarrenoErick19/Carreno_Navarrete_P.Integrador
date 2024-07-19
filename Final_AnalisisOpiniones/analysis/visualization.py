import matplotlib.pyplot as plt
import pandas as pd

def mostrar_graficos(emociones):
    # Crear gráfico de pastel para la distribución de emociones
    labels = emociones.keys()
    sizes = [len(emociones[emoción]) for emoción in emociones]
    
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title("Distribución de Emociones")

    # Mostrar los gráficos
    plt.show()
