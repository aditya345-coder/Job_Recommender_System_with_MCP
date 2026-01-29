import fitz
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

client = OpenAI()  

def extract_text_from_pdf(uploaded_file):
    """Extract text from a PDF file.

    Args:
        pdf_path (string): Path to the PDF file.

    Returns:
        string: Extracted text from the PDF file.
    """

    doc=fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text=""
    for page in doc:
        text+=page.get_text()
    return text


def ask_aimodel(question):
    """Ask a question to the AI model.

    Args:
        question (string): Question to ask the AI model.

    Returns:
        string: Answer from the AI model.
    """
    
    pass


