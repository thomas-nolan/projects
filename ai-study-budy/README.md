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
python main.py
```