# custom-chatbot
# Custom Chatbot

This project focuses on developing a personalized chatbot framework where users can create their own chatbots using custom data. The repository includes two example chatbots: the AI Career Coach and the NSigma chatbot. These examples demonstrate the capabilities and customization options of the framework.

## Features
- **Customizable Chatbots**: Users can create their own chatbots tailored to specific needs using custom data.
- **AI Integration**: Utilizes ChatGPT for intelligent conversation and responses.
- **Framework Examples**: Includes an AI Career Coach for career development advice and an NSigma chatbot for music-related interactions.
- **Flask-based Application**: Built using Flask, making it easy to deploy and extend.

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
    python run.py
    ```

## Project Structure
- **app/**: Contains the main application code.
    - **templates/**: HTML templates for the web application.
    - **static/**: Static files (CSS, JavaScript, images).
    - **\_\_init\_\_.py**: Initializes the Flask application.
    - **routes.py**: Defines the routes and logic for the web application.
- **run.py**: Entry point for running the Flask application.
- **requirements.txt**: Lists the Python dependencies for the project.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

