import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
df = pd.read_csv("data/netflix_titles.csv")

# Create a column with combined useful information
df['content'] = df['title'].fillna('') + ' ' + \
                df['description'].fillna('') + ' ' + \
                df['listed_in'].fillna('') + ' ' + \
                df['country'].fillna('')

# TF-IDF vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['content'])

# Cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Create dictionary: index → movie title
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

def recommend(title, n=5):
    if title not in indices:
        return "Movie not found"
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n+1]  # exclude the movie itself
    movie_indices = [i[0] for i in sim_scores]
    
    return df['title'].iloc[movie_indices].tolist()

# print(recommend("Blood & Water", 5))