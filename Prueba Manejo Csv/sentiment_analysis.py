#4. Vamos a crear un nuevo archivo llamado sentiment_analysis.py donde colocaremos las funciones relacionadas 
# con el análisis de sentimientos y la visualización. 

# sentiment_analysis.py


import pandas as pd
import matplotlib.pyplot as plt
from clean_data import limpiar_datos
from prepare_data_rnn import preparar_datos_para_rnn
from train_rnn import construir_entrenar_modelo_rnn
from sklearn.preprocessing import LabelEncoder

def visualizar_sentimientos(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['sentimiento'], bins=30, edgecolor='black')
    plt.title('Distribución de Sentimientos en los Comentarios')
    plt.xlabel('Polaridad del Sentimiento')
    plt.ylabel('Número de Comentarios')
    plt.show()

def realizar_analisis_sentimientos():
    df = limpiar_datos()  # Obtener el DataFrame limpio con análisis de sentimientos
    
    # Preprocesar los datos para el modelo RNN
    data, word_index = preparar_datos_para_rnn(df)
    
    # Crear etiquetas (sentimientos) basadas en la polaridad de TextBlob
    le = LabelEncoder()
    df['sentimiento_binario'] = le.fit_transform(df['sentimiento'].apply(lambda x: 1 if x >= 0 else 0))
    labels = df['sentimiento_binario'].values
    
    # Construir y entrenar el modelo RNN
    model, history = construir_entrenar_modelo_rnn(data, labels)
    
    # Evaluar el modelo (opcional)
    loss, accuracy = model.evaluate(data, labels)
    print(f'Loss: {loss}, Accuracy: {accuracy}')

def main():
    df = limpiar_datos()  # Obtener el DataFrame limpio con análisis de sentimientos
    visualizar_sentimientos(df)
    realizar_analisis_sentimientos()

if __name__ == "__main__":
    main()
