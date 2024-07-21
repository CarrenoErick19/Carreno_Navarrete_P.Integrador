import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer

def definir_modelo_rnn(vocab_size=5000, max_len=100):
    # Definir el tokenizer
    tokenizer = Tokenizer(num_words=vocab_size)
    
    # Definir el modelo RNN
    model = Sequential([
        Embedding(input_dim=vocab_size, output_dim=128, input_length=max_len),
        LSTM(units=128, return_sequences=False),
        Dense(units=5, activation='softmax')
    ])
    
    return model, tokenizer
