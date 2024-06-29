#!/usr/bin/env python3

import argparse
from preprocessing import preprocess_data
from sentimental_analysis import prepare_data, build_model, train_model
from visualization import plot_confusion_matrix, plot_sentiment_distribution
from utils import load_data

def main(input_file, preprocessed_file, epochs, batch_size):
    # Preprocesar datos
    preprocess_data(input_file, preprocessed_file)

    # Cargar datos preprocesados
    df = load_data(preprocessed_file)

    # Preparar datos para análisis de sentimientos
    X_train, X_val, y_train, y_val = prepare_data(df)

    # Construir y entrenar el modelo
    model = build_model(input_dim=5000, output_dim=128, input_length=100)
    model = train_model(model, X_train, y_train, X_val, y_val, epochs=epochs, batch_size=batch_size)

    # Hacer predicciones y visualizar resultados
    predictions = (model.predict(X_val) > 0.5).astype("int32")
    plot_confusion_matrix(y_val, predictions)
    plot_sentiment_distribution(df)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Análisis de sentimientos en comentarios de redes sociales.')
    parser.add_argument('input_file', type=str, help='Ruta del archivo CSV de entrada.')
    parser.add_argument('preprocessed_file', type=str, help='Ruta del archivo CSV preprocesado.')
    parser.add_argument('--epochs', type=int, default=5, help='Número de épocas para entrenar el modelo.')
    parser.add_argument('--batch_size', type=int, default=64, help='Tamaño del lote para entrenar el modelo.')

    args = parser.parse_args()
    main(args.input_file, args.preprocessed_file, args.epochs, args.batch_size)
