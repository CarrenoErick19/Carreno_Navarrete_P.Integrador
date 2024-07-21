import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import tensorflow as tf

def evaluar_modelo(model, test_df, tokenizer, max_len=100):
    # Vectorización
    X_test = tokenizer.texts_to_sequences(test_df['comment_limpio'])
    X_test = tf.keras.preprocessing.sequence.pad_sequences(X_test, maxlen=max_len)
    y_test = test_df['sentimiento']

    # Predicciones
    y_pred_prob = model.predict(X_test)
    y_pred = np.argmax(y_pred_prob, axis=1)

    # Métricas de evaluación
    report = classification_report(y_test, y_pred, output_dict=True)
    accuracy = report['accuracy']
    precision = report['weighted avg']['precision']
    recall = report['weighted avg']['recall']
    f1_score = report['weighted avg']['f1-score']
    
    # Matriz de confusión
    conf_matrix = confusion_matrix(y_test, y_pred)

    # Mostrar métricas
    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1 Score: {f1_score}")

    # Generar gráficos
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))

    # Matriz de confusión
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='viridis', ax=ax[0])
    ax[0].set_title('Confusion Matrix')
    ax[0].set_xlabel('Predicted')
    ax[0].set_ylabel('True')

    # Gráfico de métricas
    metrics_df = pd.DataFrame(report).transpose()
    metrics_df[['precision', 'recall', 'f1-score']].iloc[:-1].plot(kind='bar', ax=ax[1])
    ax[1].set_title('Classification Report')
    ax[1].set_ylim(0, 1)
    plt.tight_layout()
    plt.show()

    return accuracy, precision, recall, f1_score
