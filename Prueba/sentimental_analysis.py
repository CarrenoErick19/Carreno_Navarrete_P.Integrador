# 2. Este archivo contendrá las funciones para el análisis de sentimientos.

from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

def prepare_data(df):
    tokenizer = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(df['texto_limpio'])
    X = tokenizer.texts_to_sequences(df['texto_limpio'])
    X = pad_sequences(X, maxlen=100)
    y = df['sentimiento']  # Asegúrate de tener esta columna en tu CSV
    return train_test_split(X, y, test_size=0.2, random_state=42)

def build_model(input_dim, output_dim, input_length):
    model = Sequential()
    model.add(Embedding(input_dim=input_dim, output_dim=output_dim, input_length=input_length))
    model.add(LSTM(units=128, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_model(model, X_train, y_train, X_val, y_val, epochs=5, batch_size=64):
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_data=(X_val, y_val))
    return model
