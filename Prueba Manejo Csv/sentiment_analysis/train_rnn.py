#6. Crea un archivo train_rnn.py para construir y entrenar el modelo RNN.

# train_rnn.py

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split

def construir_entrenar_modelo_rnn(data, labels):
    # Dividir los datos en entrenamiento y validación
    x_train, x_val, y_train, y_val = train_test_split(data, labels, test_size=0.2, random_state=42)

    # Definir el modelo
    model = Sequential()
    model.add(Embedding(input_dim=10000, output_dim=64, input_length=data.shape[1]))
    model.add(LSTM(units=64, return_sequences=False))
    model.add(Dense(units=1, activation='sigmoid'))

    # Compilar el modelo
    model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

    # Definir callbacks
    early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

    # Entrenar el modelo
    history = model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_val, y_val), callbacks=[early_stopping])

    return model, history
