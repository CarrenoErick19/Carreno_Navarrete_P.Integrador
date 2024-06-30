#6. Crea un archivo train_rnn.py para construir y entrenar el modelo RNN.

# train_rnn.py

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from sklearn.model_selection import train_test_split

def construir_entrenar_modelo_rnn(data, labels, max_num_words=10000, max_sequence_length=100, embedding_dim=100, lstm_units=128):
    model = Sequential()
    model.add(Embedding(max_num_words, embedding_dim, input_length=max_sequence_length))
    model.add(LSTM(lstm_units, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(1, activation='sigmoid'))
    
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    
    print(model.summary())
    
    X_train, X_val, y_train, y_val = train_test_split(data, labels, test_size=0.2, random_state=42)
    
    history = model.fit(X_train, y_train,
                        batch_size=32,
                        epochs=10,
                        validation_data=(X_val, y_val))
    
    return model, history
