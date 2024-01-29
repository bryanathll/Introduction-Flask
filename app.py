from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prediction", methods = ["POST"])
def prediction():
    if request.method == "POST":
        return render_template("prediction.html")


if __name__ == "__main__":
    app.run()
