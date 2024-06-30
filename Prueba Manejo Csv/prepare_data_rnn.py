#5. Crea un nuevo archivo prepare_data_rnn.py para 
# la preparación de datos específicos para el modelo RNN.

# prepare_data_rnn.py

import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def preparar_datos_para_rnn(df, max_num_words=10000, max_sequence_length=100):
    tokenizer = Tokenizer(num_words=max_num_words)
    tokenizer.fit_on_texts(df['comentarios_limpios'])
    sequences = tokenizer.texts_to_sequences(df['comentarios_limpios'])
    
    word_index = tokenizer.word_index
    print(f'Found {len(word_index)} unique tokens.')
    
    data = pad_sequences(sequences, maxlen=max_sequence_length)
    
    return data, word_index

def predecir_sentimientos(model, word_index, nuevos_comentarios):
    tokenizer = Tokenizer(num_words=len(word_index))
    tokenizer.word_index = word_index  # Set the word_index to the provided one
    
    secuencias = tokenizer.texts_to_sequences(nuevos_comentarios)
    datos = pad_sequences(secuencias, maxlen=100)
    predicciones = model.predict(datos)
    return predicciones
