from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""
    if request.method == "POST":
        text = request.form["text"]
        lang = request.form["lang"]
        output = GoogleTranslator(source='auto', target=lang).translate(text)
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)

