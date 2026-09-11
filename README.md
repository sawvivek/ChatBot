# AI FAQ Assistant

An NLP-based FAQ Assistant developed using Python, Flask, SQLite, TF-IDF and Cosine Similarity.

## Project Goal

The project aims to develop an FAQ chatbot that can understand a user's question and return the most relevant answer from an FAQ knowledge base.

The system also provides an admin interface where FAQs can be added, edited and deleted dynamically.

## Technologies Used

* Python
* Flask
* SQLite
* NLTK
* scikit-learn
* TF-IDF
* Cosine Similarity
* HTML
* CSS
* JavaScript

## Current Features

### User Features

* Ask FAQ questions through a web interface
* Receive the most relevant answer
* Supports different wording of questions
* Handles unknown questions using a similarity threshold
* Interactive chatbot interface
* Press Enter to ask a question

### Admin Features

* View all FAQs
* Add new FAQs
* Edit existing FAQs
* Delete FAQs
* Automatically refresh the TF-IDF model after FAQ changes

## Database

The FAQ data is stored in a SQLite database.

Database file:

```text
faq.db
```

The database contains an `faqs` table with:

* `id`
* `question`
* `answer`

## NLP System

The chatbot uses a retrieval-based NLP approach.

The process is:

```text
User Question
      ↓
TF-IDF Vectorization
      ↓
Cosine Similarity
      ↓
Find Most Similar FAQ
      ↓
Check Similarity Threshold
      ↓
Return Answer
```

## Application Architecture

```text
                    ┌───────────────┐
                    │    Browser    │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    Flask      │
                    │   Web App     │
                    └───────┬───────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │    TF-IDF +       │
                  │ Cosine Similarity │
                  └─────────┬─────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    SQLite     │
                    │   FAQ Data    │
                    └───────────────┘
```

### Admin Architecture

```text
Admin
  ↓
Admin Web Interface
  ↓
Flask
  ↓
SQLite
  ↓
FAQ Database
  ↓
TF-IDF Model Refresh
```

## Project Structure

```text
AI-FAQ-Assistant/
│
├── venv/
│
├── data/
│   └── faqs.txt
│
├── templates/
│   ├── index.html
│   ├── admin.html
│   └── edit.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── app.py
├── database.py
├── faq_data.py
├── nlp_preprocessing.py
├── test_nlp.py
├── tfidf_model.py
├── chatbot.py
├── faq.db
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

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
http://127.0.0.1:5000/
```

Open the admin panel:

```text
http://127.0.0.1:5000/admin
```

## FAQ Management

The admin panel supports:

```text
Add FAQ
   ↓
SQLite
   ↓
TF-IDF Model Refresh
   ↓
Chatbot can answer the new FAQ
```

Similarly:

```text
Edit FAQ
   ↓
SQLite Update
   ↓
TF-IDF Model Refresh
   ↓
Chatbot uses updated answer
```

And:

```text
Delete FAQ
   ↓
SQLite Delete
   ↓
TF-IDF Model Refresh
   ↓
Deleted FAQ is no longer available
```

## Current Limitation

The chatbot uses TF-IDF and Cosine Similarity.

Therefore, it mainly depends on similarity between words in the user's question and the stored FAQ questions.

It may not understand deeper semantic meaning.

For example, two questions with similar meanings but very different vocabulary may not always produce the expected answer.

## Future Improvements

Possible future improvements include:

* Better NLP preprocessing
* Improved semantic similarity
* Larger FAQ knowledge base
* User and admin authentication
* Conversation history
* Better error handling
* RAG-based question answering
* Vector database
* LLM integration
* Improved UI
* Deployment to a cloud platform

## Development Progress

### Day 1

* Project setup
* Python environment
* Required packages
* Git repository

### Day 2

* FAQ dataset
* NLP preprocessing
* NLTK
* Stopword removal

### Day 3

* TF-IDF
* Cosine Similarity
* Similarity threshold
* FAQ retrieval

### Day 4

* Interactive command-line chatbot
* Conversation handling

### Day 5

* Flask web application
* HTML/CSS/JavaScript interface
* `/ask` API

### Day 6

* SQLite database
* FAQ database management
* Admin interface
* Add FAQ
* Edit FAQ
* Delete FAQ
* Dynamic TF-IDF model refresh
* Complete system testing

## Current Status

**Day 6 completed successfully.**

The project now has a working web-based NLP FAQ Assistant with SQLite database storage and an admin CRUD interface.
