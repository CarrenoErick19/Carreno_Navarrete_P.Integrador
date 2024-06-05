import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Cargar el modelo de SpaCy para español
nlp = spacy.load('es_core_news_sm')

# Inicializar el analizador de sentimientos VADER
analyzer = SentimentIntensityAnalyzer()

# Función para preprocesar tweets con SpaCy
def preprocess_tweet(tweet):
    doc = nlp(tweet)
    tokens = [token.lemma_ for token in doc if not token.is_stop]
    return ' '.join(tokens)

# Función para analizar sentimiento con VADER
def analyze_sentiment(tweet):
    return analyzer.polarity_scores(tweet)

# Ejemplo de tweets
tweets = [
    "El servicio en el hospital fue excelente y rápido.",
    "Nunca volveré a ese hospital, una experiencia terrible.",
    "Me encanto el servicio el hospital, muy buena experiencia, volvere con total seguridad"
]

# Preprocesar y analizar sentimientos de los tweets
for tweet in tweets:
    preprocessed_tweet = preprocess_tweet(tweet)
    sentiment = analyze_sentiment(preprocessed_tweet)
    print(f"Tweet: {tweet}")
    print(f"Preprocesado: {preprocessed_tweet}")
    print(f"Sentimiento: {sentiment}\n")
