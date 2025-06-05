from chatbot import load_file, get_answer

def main():
    qa_pairs = load_file("../data/notes.txt")
    print("Hi, I'm your smart AI study buddy: Ask me a question about your course (type 'exit' to quit)")
    while True:
        user_input = input('You: ')
        if user_input.lower() in ['exit', 'quit', "that's all", 'thanks']:
            print("Good luck with your studies")
            break
        response = get_answer(user_input, qa_pairs)
        print("Buddy: ", response)

if __name__ == "__main__":
    main()


