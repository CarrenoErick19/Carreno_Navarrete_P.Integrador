import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import EarlyStopping
from tqdm import tqdm

def entrenar_modelo_rnn(model, train_df, val_df, tokenizer, max_len=100, epochs=10, batch_size=16):
    # Verificar disponibilidad de GPU
    if tf.test.gpu_device_name():
        print('GPU disponible:', tf.test.gpu_device_name())
    else:
        print('GPU no disponible, utilizando CPU.')

    # Vectorización
    X_train = tokenizer.texts_to_sequences(train_df['comment_limpio'])
    X_val = tokenizer.texts_to_sequences(val_df['comment_limpio'])
    
    X_train = pad_sequences(X_train, maxlen=max_len)
    X_val = pad_sequences(X_val, maxlen=max_len)
    
    y_train = train_df['sentimiento'].astype('float32')
    y_val = val_df['sentimiento'].astype('float32')
    
    # Usar tf.data.Dataset para optimización
    train_dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train)).shuffle(len(X_train)).batch(batch_size).prefetch(tf.data.AUTOTUNE)
    val_dataset = tf.data.Dataset.from_tensor_slices((X_val, y_val)).batch(batch_size).prefetch(tf.data.AUTOTUNE)
    
    # Configurar Early Stopping con mayor paciencia
    early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
    
    # Configurar optimizador
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    
    # Entrenar el modelo con barra de progreso
    for epoch in tqdm(range(epochs), desc="Entrenando el modelo"):
        model.fit(train_dataset, validation_data=val_dataset, epochs=1, callbacks=[early_stopping], verbose=0)
        if early_stopping.stopped_epoch:
            break
    
    return model
