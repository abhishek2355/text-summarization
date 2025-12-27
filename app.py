from flask import Flask, render_template, request
from summarizer import summarize_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    summary = ""
    text = ""

    if request.method == "POST":
        text = request.form.get("paragraph")
        summary = summarize_text(text)

    return render_template("index.html", summary=summary, text=text)

if __name__ == "__main__":
    app.run(debug=True)
