from flask import Flask, render_template, request, jsonify
from chatbot import load_file, get_answer

app = Flask(__name__)
qa_pairs = load_file("../data/notes.txt")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_input = data.get("user_input", "").strip()
    if not user_input:
        return jsonify({"response": "Please type a question."})

    answer = get_answer(user_input, qa_pairs)
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(debug=True)
