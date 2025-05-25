from flask import Flask, render_template, request
from predict import Predictor
import os

app = Flask(__name__)
predictor = Predictor()
predictor.setup()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form.get("text")
    if not prompt:
        return render_template("index.html", error="Please provide a prompt.")
    
    try:
        result_path = predictor.predict(prompt=prompt)
        return render_template("index.html", image_url=result_path)
    except Exception as e:
        return render_template("index.html", error=str(e))

if __name__ == '__main__':
    app.run(debug=True)