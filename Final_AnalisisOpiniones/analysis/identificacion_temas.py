import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

def identificar_temas(df):
    if 'comment_limpio' not in df.columns:
        raise ValueError("La columna 'comment_limpio' no está presente en el DataFrame.")
    
    count_vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    count_data = count_vectorizer.fit_transform(df['comment_limpio'])

    lda = LatentDirichletAllocation(n_components=5, random_state=0)
    lda.fit(count_data)

    return lda, count_vectorizer

