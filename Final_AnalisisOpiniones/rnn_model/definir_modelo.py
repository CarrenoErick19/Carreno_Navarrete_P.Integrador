import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

def definir_modelo(max_words=10000, embedding_dim=50, input_length=100):
    model = Sequential()
    model.add(Embedding(input_dim=max_words, output_dim=embedding_dim, input_length=input_length))
    model.add(LSTM(32))  # Reducido de 64 a 32
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))
    
    return model
