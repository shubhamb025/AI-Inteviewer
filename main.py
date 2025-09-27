from flask import Flask, render_template, request
import os, json
import google.generativeai as genai
from dotenv import load_dotenv
import re
# Setup
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

app = Flask(__name__)
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_interview_questions():
    prompt = """
    You are an interviewer for an SDE Intern role. 
    Generate exactly 5 relevant interview questions in this format:
    Q1: ...
    Q2: ...
    Q3: ...
    Q4: ...
    Q5: ...
    Do not include any explanations or extra text.
    """
    response = model.generate_content(prompt)
    text = response.text.strip()

    questions = re.findall(r"(Q[1-5]:.*)", text)
    if not questions:
        questions = [line for line in text.splitlines() if line.strip()]
    return questions[:5]


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

    Return ONLY valid JSON in this format:
    {{
      "technical_score": 0-10,
      "problem_solving_score": 0-10,
      "communication_score": 0-10,
      "summary": "short text",
      "recommendation": "Hire/No Hire"
    }}
    """
    response = model.generate_content(prompt)
    text = response.text.strip()

    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except:
            return {"summary": text}
    return {"summary": text}

# Routes
@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/questions")
def questions():
    q_list = generate_interview_questions()
    return render_template("questions.html", questions=q_list)

@app.route("/evaluate", methods=["POST"])
def evaluate():
    answers = []
    for i in range(1, 6):
        ans = request.form.get(f"answer{i}", "")
        answers.append(f"Q{i}: {ans}")
    answers_text = "\n".join(answers)

    result = evaluate_candidate(answers_text)
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
