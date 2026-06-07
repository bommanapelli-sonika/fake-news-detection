from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")

def predict(text):
    pred = model.predict([text])[0]
    return "REAL NEWS" if pred == 1 else "FAKE NEWS"

@app.route("/", methods=["GET","POST"])
def home():
    result=""
    if request.method=="POST":
        news=request.form["news"]
        result=predict(news)
    return render_template("index.html", result=result)

if __name__=="__main__":
    app.run(debug=True)
