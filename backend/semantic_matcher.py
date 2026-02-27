import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def semantic_job_match(resume_text, jobs_df):

    # Combine resume + job descriptions
    documents = [resume_text] + jobs_df[1].tolist()

    # Convert text to TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    # First vector = resume
    resume_vector = tfidf_matrix[0]

    # Remaining vectors = jobs
    job_vectors = tfidf_matrix[1:]

    # Compute cosine similarity
    similarities = cosine_similarity(resume_vector, job_vectors)

    similarity_scores = similarities.flatten()

    results = []

    for i, score in enumerate(similarity_scores):
        job_title = jobs_df.iloc[i][0]
        results.append((job_title, round(float(score) * 100, 2)))

    # Sort highest first
    results.sort(key=lambda x: x[1], reverse=True)

    return results
