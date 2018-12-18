import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load Movies Metadata
metadata = pd.read_csv('../data/IMDBTop250.csv', low_memory=False)

#Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
tfidf = TfidfVectorizer(stop_words='english')

#Replace NaN with an empty string
metadata['Plot'] = metadata['Plot'].fillna('')

#Construct the required TF-IDF matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(metadata['Plot'])

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
# cosine_sim = dot(tfidf_matrix[0].T, tfidf_matrix[0])/(norm(tfidf_matrix[0])*norm(tfidf_matrix[0]))


#Construct a reverse map of indices and movie titles
indices = pd.Series(metadata.index, index=metadata['Title']).drop_duplicates()
# print(indices)


# Function that takes in movie title as input and outputs most similar movies
def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return metadata['Title'].iloc[movie_indices]

print("Recommendations for 'The Dark Knight Rises'")
print(get_recommendations('The Dark Knight Rises'))

print("Recommendations for 'The Godfather'")
print(get_recommendations('The Godfather'))
