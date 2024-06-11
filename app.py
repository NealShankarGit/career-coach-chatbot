import os
from dotenv import load_dotenv
import streamlit as st
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def load_extracted_texts(file_path):
    with open(file_path, "r") as f:
        texts = f.read()
    return texts

extracted_texts = load_extracted_texts("/Users/nealshankar/custom-chatbot/extracted_texts.txt")

def get_answer(question):
    context_length = 3500  # Adjust the context length as needed
    context = extracted_texts[:context_length]  # Use the first 3500 characters of the extracted texts for context
    prompt = f"Based on the following information from various PDF documents:\n\n{context}\n\nQuestion: {question}\nAnswer:"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )
        answer = response.choices[0].message['content'].strip()
    except openai.error.RateLimitError:
        answer = "Rate limit exceeded. Please try again later."
    except openai.error.AuthenticationError:
        answer = "Authentication error. Please check your API key."
    except openai.error.OpenAIError as e:
        answer = f"An error occurred: {str(e)}"
    
    return answer

st.title("Custom Chatbot")
question = st.text_input("Enter your question:")
if st.button("Get Answer"):
    if question:
        answer = get_answer(question)
        st.write(f"Answer: {answer}")
    else:
        st.write("Please enter a question.")
