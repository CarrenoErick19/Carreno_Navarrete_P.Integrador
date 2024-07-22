import tensorflow as tf

def definir_modelo_rnn(vocab_size, max_len):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=128, input_length=max_len),
        tf.keras.layers.LSTM(64, return_sequences=True),  # Reducir unidades LSTM
        tf.keras.layers.LSTM(64),
        tf.keras.layers.Dense(64, activation='relu'),  # Reducir unidades Dense
        tf.keras.layers.Dense(5, activation='softmax')  # 5 clases para los sentimientos
    ])
    
    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    
    return model
