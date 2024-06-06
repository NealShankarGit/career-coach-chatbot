from flask import Flask, request, jsonify
import openai
from openai import OpenAI

// call API Key

app = Flask(__name__)

@app.route('/')
def home():
    return "Custom Chatbot API. Use the /chat endpoint to interact with the chatbot."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    question = data.get('question', '')
    try:
        response = client.completions.create(model="gpt-3.5-turbo-instruct",
        prompt=question,
        max_tokens=150)
        answer = response.choices[0].text.strip()
    except openai.RateLimitError:
        answer = "Rate limit exceeded. Please try again later."
    except openai.AuthenticationError:
        answer = "Authentication error. Please check your API key."
    except openai.OpenAIError as e:
        answer = f"An error occurred: {str(e)}"

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)

