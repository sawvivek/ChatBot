from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from faq_data import load_faqs


# Load FAQ data
faqs = load_faqs()


# Extract FAQ questions
questions = []

for faq in faqs:
    questions.append(faq["question"])


# Create TF-IDF model
vectorizer = TfidfVectorizer(stop_words="english")

tfidf_matrix = vectorizer.fit_transform(questions)


# Function to find the best answer
def find_best_answer(user_question):

    # Convert user question into TF-IDF vector
    user_vector = vectorizer.transform([user_question])


    # Calculate cosine similarity
    similarity_scores = cosine_similarity(
        user_vector,
        tfidf_matrix
    )


    # Find best matching FAQ
    best_match_index = similarity_scores.argmax()


    # Get best FAQ
    best_faq = faqs[best_match_index]


    # Get similarity score
    best_score = similarity_scores[0][best_match_index]


    # Similarity threshold
    threshold = 0.2


    # Check whether the match is good enough
    if best_score < threshold:

        return "Sorry, I could not find a relevant answer."


    return best_faq["answer"]


# # Test the function
# if __name__ == "__main__":

#     question = "What is the weather today?"

#     user_vector = vectorizer.transform([question])

#     similarity_scores = cosine_similarity(
#         user_vector,
#         tfidf_matrix
#     )

#     print("Question:", question)
#     print("Similarity Scores:", similarity_scores)
#     print("Best Match Index:", similarity_scores.argmax())

#     answer = find_best_answer(question)

#     print("Answer:", answer)
