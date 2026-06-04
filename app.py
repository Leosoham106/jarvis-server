from flask import Flask, request
from google import genai
import os

app = Flask(__name__)

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

@app.route("/")
def home():
    return "Jarvis Server Online"

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json["question"]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    return {
        "answer": response.text
    }

if __name__ == "__main__":
    app.run()
