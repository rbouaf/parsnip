from flask import Flask, render_template, request
import openai

app = Flask(__name__, static_folder='static')
openai.api_key = "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"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def summarize():
    text = request.form["text"]
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please summarize the following text:\n{text}\n\nSummary:",
        temperature=0.5,
        max_tokens=1024
    )
    summary = response.choices[0].text.strip()
    return render_template("index.html", summary=summary)


if __name__ == "__main__":
    app.run(debug=False)
