import tensorflow as tf
import pickle
from tqdm import tqdm

def entrenar_y_guardar_modelo_rnn(model, X_train, y_train, X_val, y_val, tokenizer, epochs=500, batch_size=128):
    # Implementar Early Stopping
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
    
    # Compilar el modelo
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    
    # Entrenar el modelo con una barra de progreso
    with tqdm(total=epochs, desc="Training Model") as pbar:
        for epoch in range(epochs):
            history = model.fit(X_train, y_train, epochs=1, batch_size=batch_size, validation_data=(X_val, y_val), verbose=0)
            pbar.update(1)
            pbar.set_postfix(loss=history.history['loss'][-1], accuracy=history.history['accuracy'][-1], val_loss=history.history['val_loss'][-1], val_accuracy=history.history['val_accuracy'][-1])
            if early_stopping.stopped_epoch > 0:
                print(f"Early stopping at epoch {epoch+1}")
                break

    # Guardar el modelo y el tokenizer
    print("Guardando el modelo y el tokenizer...")
    model.save('modelo_rnn.keras')
    with open('tokenizer.pickle', 'wb') as handle:
        pickle.dump(tokenizer, handle)
    print("Modelo guardado en modelo_rnn.keras.")
    print("Tokenizer guardado en tokenizer.pickle.")
