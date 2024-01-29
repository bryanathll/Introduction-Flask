from flask import Flask, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route("/")
def index():
    return("hello world saudara")

if __name__ == "__main__":
    app.run()
