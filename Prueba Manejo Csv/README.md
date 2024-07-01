# Análisis de Sentimientos en Comentarios de Usuarios

Este proyecto realiza un análisis de sentimientos en comentarios de usuarios utilizando un modelo de Redes Neuronales Recurrentes (RNN).

## Requisitos

1. Python 3.7 o superior
2. Las siguientes librerías de Python:

- pandas
- matplotlib
- nltk
- textblob
- tensorflow
- scikit-learn
- tkinter

3. Se instalan las librerias requeridas:

pip install pandas matplotlib nltk textblob tensorflow scikit-learn

4. Descargar recursos adicionales para 'nltk':
Crear un archivo python y almacenar el siguiente codigo:

import nltk
nltk.download('wordnet')

Ejecutar y esperar a que se instale.

## Estructura del proyecto:

- main.py: Punto de entrada del proyecto.
- data/load_data.py: Funciones para cargar datos desde un archivo CSV.
- data/clean_data.py: Funciones para limpiar y procesar los datos.
- sentiment_analysis/prepare_data_rnn.py: Funciones para preparar datos específicos para el modelo RNN.
- sentiment_analysis/sentiment_analysis.py: Funciones para realizar análisis de sentimientos y visualización.
- sentiment_analysis/train_rnn.py: Funciones para construir y entrenar el modelo RNN.

## Ejecución:

1. Asegúrate de tener el archivo .csv de interes en una carpeta en tu directorio de trabajo. 
2. Luego añade a 'load_data.py' la ruta de dicho archivo.
3. El archivo debe tener una columna llamada comentarios con los comentarios de usuarios.
4. Ejecuta el script principal:
python main.py



