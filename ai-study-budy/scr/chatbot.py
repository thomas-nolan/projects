import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string


lemmantizer = WordNetLemmatizer()
stopwords = set(stopwords.words('english'))

def normalise(text):
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word not in string.punctuation]
    tokens = [lemmantizer.lemmatize(word) for word in tokens if word not in stopwords]
    return set(tokens)


def load_file(filename):
    qa_pairs = {}
    with open(filename, "r") as f:
        for line in f:
            if '?' in line:
                question, answer = line.strip().split('?', 1)
                qa_pairs[question.lower().strip()] = answer.strip()
    return qa_pairs

def get_answer(question, qa_pairs):
    norm_q = normalise(question)
    key = question.lower().strip()
    if key in qa_pairs:
        return qa_pairs.get(key)
    
    best_match = None
    best_score = 0
    for q in qa_pairs:
        norm_qa_question = normalise(q)
        val = jaccard_similarity(norm_qa_question, norm_q)
        if val > best_score:
            best_score = val
            best_match = q
    
    if best_score > 0.3:
        return f"(Did you mean: '{best_match}') -> {qa_pairs[best_match]}" 
    
    return "I'm sorry I am not yet equipped to answer this question."



def jaccard_similarity(set1, set2):
    intersect = set1.intersection(set2)
    union = set1.union(set2)
    if not union:
        return 0
    return len(intersect)/len(union)

