import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import tensorflow as tf

def evaluar_modelo_rnn(model, test_df, tokenizer):
    # Convertir los datos de prueba en secuencias
    X_test = tokenizer.texts_to_sequences(test_df['comment_limpio'].values)
    X_test = tf.keras.preprocessing.sequence.pad_sequences(X_test, maxlen=50)  # Usar la misma longitud que en el entrenamiento

    # Obtener las etiquetas de los datos de prueba
    y_test = test_df['sentimiento'].astype('float32')

    # Realizar predicciones
    y_pred = model.predict(X_test)
    y_pred_classes = np.argmax(y_pred, axis=1)

    # Generar la matriz de confusión y el informe de clasificación
    cm = confusion_matrix(y_test, y_pred_classes)
    cr = classification_report(y_test, y_pred_classes, target_names=['alegría', 'enojo', 'tristeza', 'satisfacción', 'insatisfacción'])

    print("Confusion Matrix:")
    print(cm)
    print("\nClassification Report:")
    print(cr)

    # Visualizar la matriz de confusión
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['alegría', 'enojo', 'tristeza', 'satisfacción', 'insatisfacción'], yticklabels=['alegría', 'enojo', 'tristeza', 'satisfacción', 'insatisfacción'])
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.show()

    return cr, cm
