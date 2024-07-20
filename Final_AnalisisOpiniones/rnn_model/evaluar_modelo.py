import tensorflow as tf
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from tensorflow.keras.preprocessing.sequence import pad_sequences

def evaluar_modelo(model, test_df, tokenizer, max_len=100):
    try:
        print("Inicio de la sección de evaluación del modelo...")
        
        print("Vectorizando datos de prueba...")
        # Vectorización
        X_test = tokenizer.texts_to_sequences(test_df['comment_limpio'])
        X_test = pad_sequences(X_test, maxlen=max_len)
        
        y_test = test_df['sentimiento']
        
        print("Realizando predicciones...")
        # Predicciones
        y_pred_prob = model.predict(X_test)
        y_pred = (y_pred_prob > 0.5).astype("int32")
        
        print("Calculando métricas...")
        # Métricas
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        
        print(f"Accuracy: {accuracy}")
        print(f"Precision: {precision}")
        print(f"Recall: {recall}")
        print(f"F1 Score: {f1}")
        
        return accuracy, precision, recall, f1
    except Exception as e:
        print(f"Error durante la evaluación del modelo: {e}")
        return None
