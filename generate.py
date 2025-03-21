import pdfplumber
import os
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

cv_path = r"D:\Smart Job Apply Assistant\Resume of Eva Akter.pdf"

def extract_cv_text(cv_path):
    """Extracts text from a PDF CV."""
    with pdfplumber.open(cv_path) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text.strip()  # Strip extra spaces/newlines


# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def query_gpt(question, cv_text, options=None):
    """Generates an answer based on the given question and CV text."""

    prompt = f"""
            You are a CV analysis expert. Your task is to extract or infer answers to given questions based on the CV text provided. 

            ### **Instructions:**
            1. **Detect answer type:**
            - If the question is about **experience, salary, years, age,notice period,education or any numerical data**, return an **integer** (default to `0` if not found).
            - Otherwise, return a **short text answer**.
            
            2. **Answering the question:**
            - If the answer exists in the CV, return it.
            - If not found:
                - Return `"N/A"` for text-based questions.
                - Return `0` for numerical questions (like `experience in years`, `salary`,`Notice period`,`Education` etc.).
            
            3. **Handling Multiple-choice Questions:**
            - If **options are provided**, return the closest matching answer from the option.
            - If no exact match is found in the CV, return random answer from the option.

            ---

            ### **CV TEXT:**
            {cv_text}

            ### **QUESTION:**
            {question}

            ### **OPTIONS:**
            {options}

            ### **ANSWER:**
            """

    response = openai.chat.completions.create(  #  Correct new API call
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a CV analysis expert. Answer accurately and concisely."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content.strip()

# cv_text = extract_cv_text(cv_path)
# question = "do you have right to work in the applying country?"
# answer = query_gpt(question, cv_text,options=["yes","no"])
# print(answer)
