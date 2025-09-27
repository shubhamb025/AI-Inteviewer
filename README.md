# 🤖 AI Interviewer

A conversational AI-powered interview system designed for SDE Intern positions. This application conducts realistic interviews with AI-generated questions and provides instant feedback with detailed evaluations.

## ✨ Features

- **🎯 AI-Generated Questions**: Dynamic interview questions covering technical, problem-solving, and behavioral aspects
- **📊 Instant Evaluation**: Comprehensive scoring system with detailed feedback
- **🎨 Modern UI**: Clean, responsive web interface

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Google API Key (free from [Google AI Studio](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd AI-Interviewer
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**

   - Create a `.env` file in the project root
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

4. **Run the application**

   ```bash
   python main.py
   ```

5. **Open your browser**
   - Navigate to `http://localhost:5000`
   - Start your AI interview!

## 🎯 How It Works

### Question Categories

- **Technical Knowledge**: Programming concepts, data structures, algorithms
- **Problem Solving**: Approach to complex challenges
- **Communication**: Clarity and structure of responses
- **Experience**: Past projects and learning
- **Behavioral**: Situational and teamwork scenarios

### Evaluation Metrics

- **Technical Score** (1-10): Programming knowledge and technical skills
- **Problem Solving Score** (1-10): Analytical thinking and solution approach
- **Communication Score** (1-10): Clarity, structure, and articulation
- **Overall Performance**: Comprehensive summary and recommendation

## 🛠️ Technical Details

### API Endpoints

- `GET /` - Welcome page
- `GET /questions` - Generate and display interview questions
- `POST /evaluate` - Process answers and return evaluation

## 🎨 User Interface

### Welcome Page

- Introduction to the AI interviewer
- Clear instructions and expectations
- Professional, friendly design

### Interview Page

- Clean question display
- Large text areas for detailed answers

### Results Page

- Visual score display
- Actionable feedback
- Professional recommendation

### Customization

You can modify the interview questions by editing the prompt in the `generate_interview_questions()` function in `main.py`.


## 🔍 Troubleshooting

### Common Issues

**"GOOGLE_API_KEY not found"**

- Ensure `.env` file exists in project root
- Verify API key is correct
- Restart the application

**"Module not found"**

- Run `pip install -r requirements.txt`
- Check Python version (3.7+ required)

**Questions not generating**

- Check internet connection
- Verify Google API key is valid
- Check console for error messages

