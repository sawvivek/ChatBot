from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from faq_data import load_faqs


# ==========================================
# PART 33 — Load FAQs
# ==========================================

faqs = load_faqs()

print("Total FAQs:", len(faqs))


# Extract FAQ questions
questions = []

for faq in faqs:
    questions.append(faq["question"])


print("Questions:", questions)


# ==========================================
# PART 34 — Create TF-IDF Matrix
# ==========================================

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(questions)


# ==========================================
# PART 35 — User Question
# ==========================================

user_question = "What is the weather of Thane today?"

print("User Question:", user_question)

user_vector = vectorizer.transform([user_question])

# Diagnostic: show the user's TF-IDF vector
print("User Vector:", user_vector.toarray())


# ==========================================
# PART 36 — Calculate Similarity
# ==========================================

similarity_scores = cosine_similarity(
    user_vector,
    tfidf_matrix
)

print("Similarity Scores:", similarity_scores)


# ==========================================
# Find Best Match
# ==========================================

best_match_index = similarity_scores.argmax()

print("Best Match Index:", best_match_index)


# ==========================================
# PART 37 — Retrieve Best FAQ
# ==========================================

best_faq = faqs[best_match_index]

best_score = similarity_scores[0][best_match_index]

print("Similarity:", best_score)


# ==========================================
# PART 44 — Similarity Threshold
# ==========================================

threshold = 0.2

if best_score < threshold:

    print("Sorry, I could not find a relevant answer.")

else:

    print("Question:", best_faq["question"])
    print("Answer:", best_faq["answer"])