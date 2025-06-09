from flask import Flask, render_template, request
from chatbot import load_file, get_answer

app = Flask(__name__)
qa_pairs = load_file("../data/notes.txt")

@app.route("/", methods = ["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = get_answer(user_input, qa_pairs)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
