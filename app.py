import os
from dotenv import load_dotenv
import streamlit as st
import openai
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader

# Load environment variables from .env
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# Set the API key for OpenAI
openai.api_key = api_key

# Load extracted texts
def load_extracted_texts(file_path):
    with open(file_path, "r") as f:
        texts = f.read()
    return texts

extracted_texts = load_extracted_texts("/Users/nealshankar/custom-chatbot/extracted_texts.txt").split('\n\n')

# Initialize LangChain components
embeddings = OpenAIEmbeddings(openai_api_key=api_key)
vector_store = FAISS.from_texts(extracted_texts, embeddings)

def get_relevant_context(question):
    retriever = vector_store.as_retriever()
    docs = retriever.get_relevant_documents(question)
    if docs:
        return docs[0].page_content
    return ""

def get_answer(question):
    context = get_relevant_context(question)
    if not context:
        return "No relevant information found in the documents."

    prompt = f"Based on the following information from various documents:\n\n{context}\n\nQuestion: {question}\nAnswer:"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=650
        )
        answer = response['choices'][0]['message']['content'].strip()
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

