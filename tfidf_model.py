from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from faq_data import load_faqs


faqs = []
questions = []
vectorizer = None
tfidf_matrix = None


def refresh_tfidf_model():
    global faqs
    global questions
    global vectorizer
    global tfidf_matrix

    faqs = load_faqs()

    questions = []

    for faq in faqs:
        questions.append(faq["question"])

    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform(questions)


def find_best_answer(user_question):

    user_vector = vectorizer.transform([user_question])

    similarity_scores = cosine_similarity(
        user_vector,
        tfidf_matrix
    )

    best_match_index = similarity_scores.argmax()

    best_faq = faqs[best_match_index]

    best_score = similarity_scores[0][best_match_index]

    threshold = 0.2

    if best_score < threshold:
        return "Sorry, I could not find a relevant answer."

    return best_faq["answer"]


refresh_tfidf_model()