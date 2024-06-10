from openai import OpenAI

client = OpenAI(api_key="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")
from flask import Flask, request, jsonify

app = Flask(__name__)

# Use the new key provided

@app.route('/')
def home():
    return "Custom Chatbot API. Use the /chat endpoint to interact with the chatbot."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    question = data.get('question', '')

    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": question}],
    max_tokens=150)

    return jsonify({"answer": response.choices[0].message.content.strip()})

if __name__ == '__main__':
    app.run(debug=True)
