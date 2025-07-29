# AI Study Buddy

This is a simple yet smart Python chatbot that answers questions from a notes file containing your course content. It uses basic natural language processing (NLP) to understand and match your given questions with the best available answers.

# How it works

- Loads question/answer pairs from a `.txt` file, where questions and answers are separated by a `?`
- Normalizes input using:
  - Tokenization (`nltk.word_tokenize`)
  - Lowercasing
  - Punctuation removal
  - Stopword removal
  - Lemmatization
- Compares user input to known questions using **Jaccard similarity**
- Returns the best-matching question along with its answer or a fallback if no match is found

# Features

- Easy to update notes by editing a simple .txt file
- Streamlined yet effective NLP processing pipeline for understanding questions
- Providines a real-time answers to the most relevant content in your notes
- Features a loading spinner animation to indicate when the bot is processing your question


# How to run

1. Make sure `data/notes.txt` exists and contains questions and answers in the format:  
   `What is a variable? A container for storing data values.`
2. Install NLTK (make sure to use version `3.8.1` for compatibility):
```bash
pip install nltk==3.8.1
```
3. Download the required NLTK data by running:
```bash
python download.py
```
4. Start the chatbot using the following script:
```bash
cd src
python app.py
```