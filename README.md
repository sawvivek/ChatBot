# AI FAQ Assistant

An NLP-based FAQ Assistant developed using Python and Flask.

## Project Goal

The project aims to develop an FAQ chatbot that can understand a user's question and return the most relevant answer from a predefined FAQ knowledge base.

The chatbot currently uses a retrieval-based NLP approach using TF-IDF and Cosine Similarity.

## Technologies

* Python
* NLP
* NLTK
* scikit-learn
* TF-IDF
* Cosine Similarity
* Flask
* HTML
* CSS
* JavaScript

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
├── data/
│   └── faqs.txt
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## How It Works

The chatbot follows a retrieval-based approach:

```text
User
 ↓
Web Interface
 ↓
JavaScript
 ↓
Flask /ask API
 ↓
TF-IDF
 ↓
Cosine Similarity
 ↓
FAQ Knowledge Base
 ↓
Best Matching FAQ
 ↓
Answer
 ↓
Web Interface
```

### Processing Steps

1. User enters a question through the web interface.
2. JavaScript sends the question to the Flask `/ask` API.
3. Flask receives the question.
4. The user's question is converted into a TF-IDF vector.
5. Cosine Similarity compares the user's question with the FAQ questions.
6. The FAQ with the highest similarity score is selected.
7. If the similarity score is below the threshold, a fallback message is returned.
8. Flask sends the answer back to JavaScript.
9. JavaScript displays the answer in the chatbot interface.

## Current Features

* FAQ knowledge base
* NLP preprocessing
* TF-IDF-based text representation
* Cosine Similarity
* Best FAQ matching
* Similarity threshold
* Flask web interface
* `/ask` API endpoint
* Interactive chatbot
* User and bot messages
* Enter-to-send support
* Greeting handling
* Empty input handling
* Unknown-question handling
* Case-insensitive input
* Input whitespace handling
* Scrollable chat area

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

### Example

```text
User:
How do I apply for admission?

Bot:
You can apply for admission through the college admission portal.
```

## Running the Project

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Run the Flask application:

```powershell
python app.py
```

Open the application in a browser:

```text
http://127.0.0.1:5000
```

## Current Limitation

The current chatbot uses TF-IDF and Cosine Similarity. Therefore, it mainly depends on word overlap between the user's question and the FAQ questions.

Very short questions or questions using completely different vocabulary may not always produce the expected answer.

## Future Improvements

* Improve NLP preprocessing
* Add more FAQ data
* Improve semantic understanding
* Add database integration
* Add authentication
* Add student and company/employee user interfaces
* Add RAG-based retrieval
* Add an LLM for more advanced responses

## Current Status

**Day 5 - Flask web interface completed.**

The NLP-based FAQ engine from Day 3 and the interactive chatbot from Day 4 have been successfully connected to a Flask web interface.
