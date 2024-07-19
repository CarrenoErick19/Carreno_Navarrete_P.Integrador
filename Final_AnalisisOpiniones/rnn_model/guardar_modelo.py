import tensorflow as tf
import pickle

def guardar_modelo(model, tokenizer, model_path='modelo_rnn.keras', tokenizer_path='tokenizer.pickle'):
    print(f"Guardando el modelo en {model_path}...")
    model.save(model_path)
    print(f"Modelo guardado en {model_path}.")
    
    print(f"Guardando el tokenizer en {tokenizer_path}...")
    with open(tokenizer_path, 'wb') as handle:
        pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"Tokenizer guardado en {tokenizer_path}.")
