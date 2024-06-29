#4. Vamos a crear un nuevo archivo llamado sentiment_analysis.py donde colocaremos las funciones relacionadas 
# con el análisis de sentimientos y la visualización. 

import pandas as pd
import matplotlib.pyplot as plt
from clean_data import limpiar_datos

def visualizar_sentimientos(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['sentimiento'], bins=30, edgecolor='black')
    plt.title('Distribución de Sentimientos en los Comentarios')
    plt.xlabel('Polaridad del Sentimiento')
    plt.ylabel('Número de Comentarios')
    plt.show()

def main():
    df = limpiar_datos()  # Obtener el DataFrame limpio con análisis de sentimientos
    visualizar_sentimientos(df)

if __name__ == "__main__":
    main()
