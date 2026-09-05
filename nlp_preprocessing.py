import string
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()

    text = text.translate(
        str.maketrans('', '', string.punctuation)
    )

    tokens = text.split()

    filtered_tokens = []

    for word in tokens:
        if word not in stop_words:
            filtered_tokens.append(word)

    return filtered_tokens
