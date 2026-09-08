# AI FAQ Assistant

An NLP-based FAQ Assistant developed using Python.

## Project Goal

The project aims to develop an FAQ chatbot that can understand a user's question and return the most relevant answer from a predefined FAQ knowledge base.

## Technologies

* Python
* NLP
* scikit-learn
* TF-IDF
* Cosine Similarity
* Flask
* SQLite

## Project Structure

```text
AI-FAQ-Assistant/
│
├── app.py
├── chatbot.py
├── faq_data.py
├── nlp_preprocessing.py
├── test_nlp.py
├── tfidf_model.py
├── requirements.txt
├── .gitignore
├── README.md
│
└── data/
    └── faqs.txt
```

## How It Works

The chatbot follows a retrieval-based approach:

1. User enters a question.
2. FAQ questions are loaded from the knowledge base.
3. TF-IDF converts FAQ questions into numerical vectors.
4. The user's question is also converted into a TF-IDF vector.
5. Cosine Similarity compares the user's question with the FAQ questions.
6. The FAQ with the highest similarity score is selected.
7. The corresponding answer is returned to the user.
8. If the similarity score is below the threshold, the chatbot returns a fallback message.

## Current Features

* FAQ knowledge base
* NLP preprocessing
* TF-IDF-based text representation
* Cosine Similarity
* Best FAQ matching
* Similarity threshold
* Interactive chatbot
* Greeting handling
* Empty input handling
* Exit command
* Unknown-question handling
* Case-insensitive input
* Input whitespace handling

## Example Questions

The chatbot can answer questions related to:

* Admission
* Admission requirements
* Required documents
* Admission status
* Admission fees
* College contact information
* College location
* Available courses

## Current Status

Day 4 - Complete NLP-based interactive FAQ chatbot implemented.

## Current Limitation

The current chatbot uses TF-IDF and Cosine Similarity. Therefore, it mainly depends on word overlap between the user's question and the FAQ questions.

Very short questions or questions using completely different vocabulary may not always produce the expected answer.

## Future Improvements

* Improve NLP preprocessing
* Add more FAQ data
* Improve semantic understanding
* Add a web interface using Flask
* Add database integration
* Add RAG-based retrieval
* Add an LLM for more advanced responses
