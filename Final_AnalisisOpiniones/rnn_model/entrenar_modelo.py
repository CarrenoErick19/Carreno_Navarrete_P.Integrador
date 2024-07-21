import tensorflow as tf

def entrenar_modelo_rnn(model, train_df, val_df, tokenizer, epochs=10):
    # Convertir los datos de entrenamiento y validación en secuencias
    X_train = tokenizer.texts_to_sequences(train_df['comment_limpio'].values)
    X_train = tf.keras.preprocessing.sequence.pad_sequences(X_train, maxlen=100)
    y_train = train_df['sentimiento']

    X_val = tokenizer.texts_to_sequences(val_df['comment_limpio'].values)
    X_val = tf.keras.preprocessing.sequence.pad_sequences(X_val, maxlen=100)
    y_val = val_df['sentimiento']

    # Compilar el modelo
    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    # Entrenar el modelo
    model.fit(X_train, y_train, epochs=epochs, batch_size=64, validation_data=(X_val, y_val))

    return model, tokenizer
