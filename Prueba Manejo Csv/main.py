# Este archivo será el punto de entrada del proyecto y desde 
# donde se importaran las funciones necesarias de los otros archivos.

from data.load_data import mostrar_datos_csv
from data.clean_data import limpiar_datos
from sentiment_analysis.sentiment_analysis import realizar_analisis_sentimientos, visualizar_sentimientos
from sentiment_analysis.prepare_data_rnn import preparar_datos_para_rnn, predecir_sentimientos
from sentiment_analysis.train_rnn import construir_entrenar_modelo_rnn

def main():
    # Mostrar datos del CSV
    df = mostrar_datos_csv()
    # Limpiar datos
    df = limpiar_datos()
    # Realizar análisis de sentimientos y entrenar el modelo RNN
    realizar_analisis_sentimientos()
    # Preparar datos para RNN
    data, word_index = preparar_datos_para_rnn(df)
    # Entrenar modelo RNN
    model, history = construir_entrenar_modelo_rnn(data, df['sentimiento'])
    
    # Nuevos comentarios para prueba
    nuevos_comentarios = [
        "El producto es excelente, muy recomendado",
        "El servicio fue terrible, no volveré a comprar aquí",
        "Me encantó la experiencia de compra, todo perfecto",
        "La calidad del producto deja mucho que desear"
    ]
    
    # Predecir sentimientos
    predicciones = predecir_sentimientos(model, word_index, nuevos_comentarios)
    print(f"Predicciones: {predicciones}")

if __name__ == "__main__":
    main()
