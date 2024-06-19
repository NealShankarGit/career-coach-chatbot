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

4. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

## Project Structure
- **app/**: Contains the main application code.
    - **templates/**: HTML templates for the web application. (If still used, otherwise remove)
    - **static/**: Static files (CSS, JavaScript, images). (If still used, otherwise remove)
    - **\_\_init\_\_.py**: Initializes the Flask application. (If still used, otherwise remove)
    - **routes.py**: Defines the routes and logic for the web application. (If still used, otherwise remove)
- **app.py**: Entry point for running the Streamlit application.
- **extract_texts.py**: Script to extract text from PDFs into a CSV file.
- **requirements.txt**: Lists the Python dependencies for the project.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
