from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
import re

# Load API key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not set in .env")

# Configure model
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# Flask app setup
app = Flask(__name__)
CORS(app)

# Prompts for each section
section_prompts = {
    "education": (
        "Extract the following attributes:\n"
        "- id\n"
        "- institution\n"
        "- location \n"
        "- degree\n"
        "- gpa (if available)\n"
        "- startDate\n"
        "- endDate\n\n"
    ),
    "experience": (
        "Extract the following attributes:\n"
        "- title\n"
        "- company\n"
        "- id\n"
        "- startDate\n"
        "- endDate\n"
        "- link\n"
        "- points (list of bullet points in detail each point of one line)\n\n"
    ),
    "projects": (
        "Extract the following attributes:\n"
        "- projectTitle\n"
        "- description\n"
        "- technologies (list)\n"
        "- role\n"
        "- startDate\n"
        "- endDate\n\n"
    ),
    "skills": (
        "Extract the following attributes:\n"
        "- softSkills (list)\n"
        "- languages (note these are computer languages) (list)\n\n"
        "- platforms (list)\n\n"
        "- frameworks (list)\n\n"
        "- tools ( (list)\n\n"
        
    ),
    "certificates": (
        "Extract the following attributes:\n"
        "- id\n"
        "- name\n"
        "- link {text, url}}\n"
        "- date\n"
        "- description\n\n"
        "Note: You return only one object that with most appropriate certification"
    ),
    "achievements": (
        "Extract the following attributes:\n"
        "- title\n"
        "- description\n"
        "- date (if available)\n\n"
    ),
    "interests": (
        "Extract the following attributes:\n"
        "- interests (list of interests or hobbies)\n\n"
    ),
    "languages": (
        "Extract the following attributes:\n"
        "- language\n"
        "- proficiency\n\n"
    ),
    "customSections": (
        "Extract the following attributes:\n"
        "- id\n"
        "- title\n"
        "- content\n"
       
    )
}


@app.route('/')
def home():
    return 'Resume Builder API is running!'


@app.route('/generate_resume_section', methods=['POST'])
def generate_resume_section():
    try:
        data = request.get_json()
        
        section_name = data.get('sectionName')
        question_answers = data.get('questionAnswers')

        if not section_name or not question_answers:
            return jsonify({'error': 'Missing sectionName or questionAnswers'}), 400

        if section_name not in section_prompts:
            return jsonify({'error': f'Unsupported sectionName: {section_name}'}), 400

        qa_string = "\n".join([
            f"Q: {q}\nA: {a if a.strip() else 'No answer provided.'}"
            for q, a in question_answers.items()
        ])

        prompt = (
            f"You are a resume-building assistant. Based on the answers related to the '{section_name}' section, "
            f"extract structured data in JSON format with the following attributes. "
            f"If any attribute is not available, set its value to null.\n\n"
            f"{section_prompts[section_name]}"
            f"Answers:\n{qa_string}\n\n"
            "Output a list of one dictionary item (even if you find multiples but return one). Return only one in the JSON."
        )

        response = model.generate_content(prompt)

        raw_text = response.text.strip()
        cleaned_text = re.sub(r"```json|```", "", raw_text, flags=re.IGNORECASE).strip()

        # Optional: print for debugging
        structured_data = json.loads(cleaned_text)
        
        return jsonify({ 'sectionData': structured_data })

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
