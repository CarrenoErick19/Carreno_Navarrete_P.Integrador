#Este archivo almacena las funciones relacionadas con el análisis de sentimientos 
# y su visualización. 

# sentiment_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
from data.clean_data import limpiar_datos
from sentiment_analysis.prepare_data_rnn import preparar_datos_para_rnn, predecir_sentimientos
from sentiment_analysis.train_rnn import construir_entrenar_modelo_rnn
from sklearn.preprocessing import LabelEncoder

def visualizar_sentimientos(df):
    if 'sentimiento' not in df.columns:
        raise ValueError("La columna 'sentimiento' no se encuentra en el DataFrame")
        
    plt.figure(figsize=(10, 6))
    plt.hist(df['sentimiento'], bins=30, edgecolor='black')
    plt.title('Distribución de Sentimientos en los Comentarios')
    plt.xlabel('Polaridad del Sentimiento')
    plt.ylabel('Número de Comentarios')
    plt.show()

def plot_training_history(history):
    # Plot training & validation accuracy values
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')

    # Plot training & validation loss values
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')

    plt.show()

def plot_predictions(predicciones, nuevos_comentarios):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(nuevos_comentarios)), predicciones.flatten())
    plt.title('Predicciones de Sentimientos para Nuevos Comentarios')
    plt.xlabel('Índice del Comentario')
    plt.ylabel('Probabilidad de Sentimiento Positivo')
    plt.show()

def realizar_analisis_sentimientos():
    df = limpiar_datos()  # Obtener el DataFrame limpio con análisis de sentimientos
    
    # Preprocesar los datos para el modelo RNN
    data, tokenizer = preparar_datos_para_rnn(df)
    
    # Crear etiquetas (sentimientos) basadas en la polaridad de TextBlob
    le = LabelEncoder()
    df['sentimiento_binario'] = le.fit_transform(df['sentimiento'].apply(lambda x: 1 if x >= 0 else 0))
    labels = df['sentimiento_binario'].values
    
    # Construir y entrenar el modelo RNN
    model, history = construir_entrenar_modelo_rnn(data, labels)
    
    # Evaluar el modelo (opcional)
    loss, accuracy = model.evaluate(data, labels)
    print(f'Loss: {loss}, Accuracy: {accuracy}')
    
    # Visualizar curvas de entrenamiento
    plot_training_history(history)

    # Visualizar sentimientos
    visualizar_sentimientos(df)

    # Visualizar predicciones (suponiendo que tienes algunos nuevos comentarios)
    nuevos_comentarios = [
        "La salud debería ser gratuita.",
        "Los hospitales públicos son buenos.",
        "Privatizar la salud es peligroso.",
        "Necesitamos mejor atención médica."
    ]
    predicciones = predecir_sentimientos(model, tokenizer, nuevos_comentarios)
    print(f'Predicciones: {predicciones}')
    plot_predictions(predicciones, nuevos_comentarios)

def main():
    df = limpiar_datos()  # Obtener el DataFrame limpio con análisis de sentimientos
    realizar_analisis_sentimientos()

if __name__ == "__main__":
    main()
