from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def identificar_temas(df, num_temas=5):
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    dtm = vectorizer.fit_transform(df['comentarios_limpios'])
    
    lda = LatentDirichletAllocation(n_components=num_temas, random_state=42)
    lda.fit(dtm)
    
    temas = {}
    for index, topic in enumerate(lda.components_):
        temas[f'Tema {index + 1}'] = [vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]]
    
    return temas
