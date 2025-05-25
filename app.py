from flask import Flask, render_template, request
import replicate
import os

app = Flask(__name__)

# Set the API token (make sure this token is valid)
os.environ["REPLICATE_API_TOKEN"] = "r8_2tWRxCB6i8tAG66zPpEQgmtovzRWde30K67Eb"

# Initialize replicate client
replicate_client = replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form.get("text")
    
    if not prompt:
        return render_template("index.html", error="No prompt provided.")
    
    print("Generating video for prompt:", prompt)

    try:
        model_version = "amjad72majeed/video-generation"
        output = replicate_client.run(
            model_version,
            input={"prompt": prompt}
        )
        return render_template("index.html", video_url=output)
    
    except Exception as e:
        print("Error:", str(e))
        return render_template("index.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)