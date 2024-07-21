import tensorflow as tf

def entrenar_modelo_rnn(model, X_train, y_train, X_val, y_val, tokenizer, epochs=10, batch_size=64, verbose=1, callbacks=None):
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_data=(X_val, y_val), verbose=verbose, callbacks=callbacks)
    return model, tokenizer
