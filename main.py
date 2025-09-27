import google.generativeai as genai
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import json

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

app = Flask(__name__)
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_interview_questions():
    prompt = """
    You are an interviewer for an SDE Intern role. Generate 5 relevant interview questions that cover:
    1. Technical knowledge (programming, data structures, algorithms)
    2. Problem-solving approach
    3. Communication skills
    4. Experience and projects
    5. Behavioral/situational questions

    Return the questions in this exact format:
    Q1: [Question 1]
    Q2: [Question 2]
    Q3: [Question 3]
    Q4: [Question 4]
    Q5: [Question 5]
    """
    response = model.generate_content(prompt)
    return response.text.strip()

def evaluate_candidate(responses):
    prompt = f"""
    You are an interviewer for an SDE Intern role.

    Candidate's answers:
    {responses}

    Task:
    1. Evaluate Technical Knowledge, Problem-Solving, and Communication.
    2. Give a score from 1 to 10 for each.
    3. Provide a short performance summary.
    4. Give a final recommendation (Hire or No Hire).

    Return the result strictly in JSON format like this:
    {{
      "technical_score": 0-10,
      "problem_solving_score": 0-10,
      "communication_score": 0-10,
      "summary": "short text",
      "recommendation": "Hire/No Hire"
    }}
    """
    response = model.generate_content(prompt)
    return response.text.strip()

@app.route("/questions", methods=["GET"])
def get_questions():
    questions_text = generate_interview_questions()

    # Split by lines that start with Q1, Q2, etc.
    questions_list = [q.strip() for q in questions_text.split("\n") if q.strip().startswith("Q")]
    return jsonify({"questions": questions_list})

@app.route("/evaluate", methods=["POST"])
@app.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.json
    responses = data.get("answers", "")
    result_text = evaluate_candidate(responses)

    import json
    try:
        result_json = json.loads(result_text)
    except:
        result_json = {"raw_output": result_text}

    return jsonify(result_json)


if __name__ == "__main__":
    app.run(debug=True)
