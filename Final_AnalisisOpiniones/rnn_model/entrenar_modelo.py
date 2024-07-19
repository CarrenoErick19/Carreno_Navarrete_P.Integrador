import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import EarlyStopping
from tqdm import tqdm

def entrenar_modelo_rnn(model, train_df, val_df, tokenizer, max_len=100, epochs=500):
    # Verificar disponibilidad de GPU
    if tf.test.gpu_device_name():
        print('GPU disponible:', tf.test.gpu_device_name())
    else:
        print('GPU no disponible, utilizando CPU.')

    # Vectorización
    X_train = tokenizer.texts_to_sequences(train_df['comentarios_limpios'])
    X_val = tokenizer.texts_to_sequences(val_df['comentarios_limpios'])
    
    X_train = pad_sequences(X_train, maxlen=max_len)
    X_val = pad_sequences(X_val, maxlen=max_len)
    
    y_train = train_df['sentimiento']
    y_val = val_df['sentimiento']
    
    # Configurar Early Stopping
    early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
    
    # Entrenar el modelo con barra de progreso
    for epoch in tqdm(range(epochs), desc="Entrenando el modelo"):
        model.fit(X_train, y_train, epochs=1, validation_data=(X_val, y_val), batch_size=32, callbacks=[early_stopping], verbose=0)
    
    return model
