from data.data_cleaning import cargar_csv, limpiar_datos, vectorizar_texto, mostrar_resultados
from data.data_split import dividir_datos
from rnn_model.definir_modelo import definir_modelo
from rnn_model.entrenar_modelo import entrenar_modelo_rnn
from rnn_model.guardar_modelo import guardar_modelo
from rnn_model.evaluar_modelo import evaluar_modelo
from analysis.analisis_sentimiento import analizar_sentimientos
from analysis.identificacion_temas import identificar_temas
from analysis.comparacion import comparar_resultados
from analysis.visualization import mostrar_graficos
import tensorflow as tf
import numpy as np

if __name__ == "__main__":
    try:
        print("Cargando datos...")
        file_name = 'datos_combinados_1.csv'  # Cambiar el nombre del archivo CSV aquí
        df = cargar_csv(file_name)
        
        print("Limpiando datos...")
        df_limpio = limpiar_datos(df)
        
        # Verificar la columna 'comment_limpio'
        print("Columnas disponibles después de limpiar los datos:", df_limpio.columns)
        if 'comment_limpio' not in df_limpio.columns:
            raise ValueError("La columna 'comment_limpio' no está presente en el DataFrame.")
        
        # Convertir las etiquetas de sentimiento a valores numéricos
        df_limpio['sentimiento'] = df_limpio['comment'].apply(lambda x: 1 if 'bueno' in x else 0 if 'malo' in x else 2)
        
        # Agregar una columna de 'aspecto' para fines de ejemplo
        df_limpio['aspecto'] = df_limpio['comment'].apply(lambda x: 'features' if 'feature' in x else 'bugs' if 'bug' in x else 'other')

        print("Dividiendo datos en entrenamiento, validación y prueba...")
        train_df, val_df, test_df = dividir_datos(df_limpio)
        
        print("Definiendo el modelo...")
        model = definir_modelo()
        
        print("Tokenizando texto...")
        tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=10000)
        tokenizer.fit_on_texts(train_df['comment_limpio'])
        
        print("Entrenando el modelo...")
        model = entrenar_modelo_rnn(model, train_df, val_df, tokenizer, epochs=100)  # Reduciendo epochs a 100 temporalmente
        
        print("Guardando el modelo y el tokenizer...")
        guardar_modelo(model, tokenizer)
        
        print("Evaluando el modelo...")
        evaluar_modelo(model, test_df, tokenizer)
        
        print("Análisis de sentimientos...")
        print("Columnas disponibles antes del análisis de sentimientos:", df_limpio.columns)
        emociones = analizar_sentimientos(df_limpio)
        
        print("Identificación de temas...")
        lda, count_vectorizer = identificar_temas(df_limpio)
        
        print("Comparando resultados con datos anteriores...")
        nuevos_resultados = {
            'emociones': emociones,
            'temas': lda.components_
        }
        comparacion = comparar_resultados(nuevos_resultados)
        
        print("Mostrando gráficos de estadísticas...")
        mostrar_graficos(df_limpio, emociones, count_vectorizer)
        
        print("Vectorizando texto limpio para mostrar resultados...")
        tfidf_matrix, feature_names = vectorizar_texto(df_limpio)
        mostrar_resultados(df_limpio, tfidf_matrix, feature_names)
        
        print("Ejecución completada.")
    except Exception as e:
        print(f"Error durante la ejecución del programa: {e}")
