def load_file(filename):
    qa_pairs = {}
    with open(filename, "r") as f:
        for line in f:
            if '?' in line:
                question, answer = line.strip().split('?', 1)
                qa_pairs[question.lower().strip()] = answer.strip()
    return qa_pairs

def get_answer(question, qa_pairs):
    question = question.lower().strip()
    return qa_pairs.get(question, "I'm sorry, I'm not yet equipped to answer this question.")
