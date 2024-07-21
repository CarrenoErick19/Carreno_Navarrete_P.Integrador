import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluar_modelo(model, test_df, tokenizer, max_len=100):
    X_test = tokenizer.texts_to_sequences(test_df['comment_limpio'])
    X_test = pad_sequences(X_test, maxlen=max_len)
    
    y_test = test_df['sentimiento'].astype('int32')  # Cambiado a int32
    
    y_pred = model.predict(X_test)
    y_pred_classes = np.argmax(y_pred, axis=1)
    
    accuracy = accuracy_score(y_test, y_pred_classes)
    precision = precision_score(y_test, y_pred_classes, average='weighted', zero_division=0)
    recall = recall_score(y_test, y_pred_classes, average='weighted', zero_division=0)
    f1 = f1_score(y_test, y_pred_classes, average='weighted', zero_division=0)
    
    return accuracy, precision, recall, f1
