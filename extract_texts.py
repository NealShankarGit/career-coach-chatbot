import fitz  # PyMuPDF
import os

def extract_text_from_pdfs(folder_path):
    texts = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            full_path = os.path.join(folder_path, filename)
            with fitz.open(full_path) as doc:
                text = ""
                for page in doc:
                    text += page.get_text()
                texts.append(text)
    return texts

if __name__ == "__main__":
    folder_path = "/Users/nealshankar/Desktop/EGN 4912/Data/DataPDFs"
    pdf_texts = extract_text_from_pdfs(folder_path)
    with open("extracted_texts.txt", "w") as f:
        for text in pdf_texts:
            f.write(text + "\n---\n")
