# Este archivo ejecutará una prueba simple para verificar que TextBlob 
# esté funcionando correctamente.

# test_textblob.py

from textblob import TextBlob

# Ejemplos de comentarios
comentarios = [
    "Este es un buen producto",
    "No me gustó el servicio",
    "Es una experiencia maravillosa",
    "La calidad es terrible"
]

# Analizar el sentimiento de cada comentario
for comentario in comentarios:
    sentimiento = TextBlob(comentario).sentiment.polarity
    print(f"Comentario: {comentario}, Sentimiento: {sentimiento}")

