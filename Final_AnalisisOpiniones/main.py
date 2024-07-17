from data.data_cleaning import cargar_csv, limpiar_datos, vectorizar_texto, mostrar_resultados
from data.data_split import dividir_datos
from rnn_model.definir_modelo import definir_modelo
from rnn_model.entrenar_modelo import entrenar_modelo_rnn
from rnn_model.guardar_modelo import guardar_modelo
import tensorflow as tf

if __name__ == "__main__":
    file_name = 'comentarios_reddit.csv'
    df = cargar_csv(file_name)
    df_limpio = limpiar_datos(df)
    
    # Dividir datos en entrenamiento, validación y prueba
    train_df, val_df, test_df = dividir_datos(df_limpio)
    
    # Agregar una columna de 'sentimiento' para fines de ejemplo
    # En una implementación real, esta columna debe ser creada según los datos específicos
    df_limpio['sentimiento'] = df_limpio['comentarios'].apply(lambda x: 1 if 'bueno' in x else 0)
    
    # Definir el modelo
    model = definir_modelo()
    
    # Tokenizar texto
    tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=10000)
    tokenizer.fit_on_texts(train_df['comentarios_limpios'])
    
    # Entrenar el modelo
    model = entrenar_modelo_rnn(model, train_df, val_df, tokenizer)
    
    # Guardar el modelo y el tokenizer
    guardar_modelo(model, tokenizer)
    
    # Vectorizar todo el texto limpio para mostrar los resultados
    tfidf_matrix, feature_names = vectorizar_texto(df_limpio)
    mostrar_resultados(df_limpio, tfidf_matrix, feature_names)
