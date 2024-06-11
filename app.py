import streamlit as st
import openai

# Load your extracted texts
def load_extracted_texts(file_path):
    with open(file_path, "r") as f:
        texts = f.read()
    return texts

extracted_texts = load_extracted_texts("/Users/nealshankar/custom-chatbot/extracted_texts.txt")

openai.api_key = "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"

def get_response(question):
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
            max_tokens=500  # Increase max_tokens to allow longer answers
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
    answer = get_response(question)
    st.write("Answer:", answer)
