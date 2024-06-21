# Career Coach Chatbot

This project focuses on developing a personalized chatbot framework designed to provide career guidance for Computer Science students entering the job market. The Career Coach Chatbot leverages advanced AI to offer personalized advice, career development tips, and interview preparation assistance.

## Features
- **Customizable Chatbots**: Tailored specifically to provide career guidance for Computer Science students.
- **AI Integration**: Utilizes ChatGPT for intelligent conversation and responses.
- **Streamlit-based Application**: Built using Streamlit, making it easy to deploy and extend.

## Getting Started

### Prerequisites
- Python 3.7+
- Virtualenv

### Installation
1. **Clone the Repository**:
    ```bash
    git clone git@github.com:NealShankarGit/custom-chatbot.git
    cd custom-chatbot
    ```

2. **Create and Activate Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Unix/macOS
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**:
    Create a `.env` file in the root directory of the project and add your OpenAI API key:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key_here
    ```

5. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

### Using Custom Data
To use your own PDF files for extracting text and providing custom data to the chatbot:

1. **Place Your PDFs**:
    Place your PDF files in a directory of your choice on your system.

2. **Update File Path**:  
    Open the `extract_texts.py` script and update the file path to point to your directory containing the PDFs. For example:
    ```python
    import os
    from langchain.document_loaders import PyPDFLoader

    # Update this line with your PDF directory
    pdf_directory = '/path/to/your/pdf/directory'
    ```

3. **Run the Script**:  
    Extract the texts from your PDFs by running the `extract_texts.py` script:
    ```bash
    python extract_texts.py
    ```
    This will create a CSV file with the extracted text data, which the chatbot will use.

## Project Structure

LICENSE  
README.md  
app.py  
bfg.jar  
create_env_file.py  
extract_texts.py  
extracted_texts.txt  
requirements.txt  
venv/

- **LICENSE**: License for the project.
- **README.md**: This file.
- **app.py**: Entry point for running the Streamlit application.
- **bfg.jar**: Tool for removing large or sensitive files from Git history.
- **create_env_file.py**: Script to create a `.env` file for environment variables.
- **extract_texts.py**: Script to extract text from PDFs into a CSV file.
- **extracted_texts.txt**: Sample text file used for testing.
- **requirements.txt**: Lists the Python dependencies for the project.
- **venv/**: Virtual environment directory (not to be committed to Git).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
