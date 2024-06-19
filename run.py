from flask import Flask, request, jsonify
import openai
from openai import OpenAI

client = OpenAI(api_key="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")

app = Flask(__name__)

def load_extracted_texts(file_path):
    with open(file_path, "r") as f:
        texts = f.read()
    return texts

extracted_texts = load_extracted_texts("extracted_texts.txt")

@app.route('/')
def home():
    return "Custom Chatbot API. Use the /chat endpoint to interact with the chatbot."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    question = data.get('question', '')
    context_length = 3500
    context = extracted_texts[:context_length]
    prompt = f"Based on the following information from various PDF documents:\n\n{context}\n\nQuestion: {question}\nAnswer:"

    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150)
        answer = response.choices[0].message.content.strip()
    except openai.RateLimitError:
        answer = "Rate limit exceeded. Please try again later."
    except openai.AuthenticationError:
        answer = "Authentication error. Please check your API key."
    except openai.OpenAIError as e:
        answer = f"An error occurred: {str(e)}"

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
