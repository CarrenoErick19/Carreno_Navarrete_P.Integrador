#1. Este archivo será el punto de entrada de tu proyecto y desde 
# donde importarás las funciones necesarias de los otros archivos.

# main.py

from load_data import mostrar_datos_csv
from clean_data import limpiar_datos
from sentiment_analysis import realizar_analisis_sentimientos, visualizar_sentimientos
from prepare_data_rnn import preparar_datos_para_rnn, predecir_sentimientos
from train_rnn import construir_entrenar_modelo_rnn

def main():
    # Mostrar datos del CSV
    mostrar_datos_csv()
    
    # Limpiar datos
    df = limpiar_datos()

    # Realizar análisis de sentimientos y entrenar el modelo RNN
    realizar_analisis_sentimientos()
    
    # Preparar datos para RNN
    data, word_index = preparar_datos_para_rnn(df)

    # Entrenar modelo RNN
    model = construir_entrenar_modelo_rnn(data, df['sentimiento'])
    
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
