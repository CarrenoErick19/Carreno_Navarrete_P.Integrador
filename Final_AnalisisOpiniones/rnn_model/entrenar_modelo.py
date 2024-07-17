import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

def entrenar_modelo_rnn(model, train_df, val_df, tokenizer, max_len=100, epochs=500):
    # Vectorización
    X_train = tokenizer.texts_to_sequences(train_df['comentarios_limpios'])
    X_val = tokenizer.texts_to_sequences(val_df['comentarios_limpios'])
    
    X_train = pad_sequences(X_train, maxlen=max_len)
    X_val = pad_sequences(X_val, maxlen=max_len)
    
    y_train = train_df['sentimiento']
    y_val = val_df['sentimiento']
    
    # Entrenar el modelo
    model.fit(X_train, y_train, epochs=epochs, validation_data=(X_val, y_val), batch_size=32)
    
    return model
