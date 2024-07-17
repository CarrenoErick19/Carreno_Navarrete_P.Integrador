import tensorflow as tf
import pickle

def guardar_modelo(model, tokenizer, model_path='modelo_rnn.h5', tokenizer_path='tokenizer.pickle'):
    model.save(model_path)
    with open(tokenizer_path, 'wb') as handle:
        pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
