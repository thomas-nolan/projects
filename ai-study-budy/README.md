# AI Study Buddy

This is a simple Python chatbot that answers questions from a notes file containing course details.

## How it works

- Loads question/answer pairs from a `.txt` file, in which questions and answers are seperated by a '?'
- Matches input to known questions
- Returns the answer or a fallback message if it cannot match input to a question

## How to run

1. Make sure `data/notes.txt` exists
2. Run the script:

```bash
cd src
python main.py
```