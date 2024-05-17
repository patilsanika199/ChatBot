import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load your dataset
data = pd.read_csv('chats.csv')

# Create the TF-IDF model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['question'])

# Save the vectorizer and the matrix
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

with open('tfidf_matrix.pkl', 'wb') as f:
    pickle.dump(X, f)

# Optionally save the dataframe
data.to_pickle('chats.pkl')
