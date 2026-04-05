# Job Interview Practice System

A real‑time, AI‑powered web application that simulates a job interview.  
The system uses your webcam to analyse facial expressions and hand gestures, presents interview questions based on your chosen job role and language, and provides instant feedback with a final score.

## Features

### Free Version (Text-based)
- 8 job positions (Software Engineer, Data Analyst, ...) with 40 questions each (20 English + 20 Myanmar).
- Randomly selects 5 questions per session.
- Hand gesture recognition (1,2,3 fingers) to select answers.
- Real‑time confidence score based on eye contact (30%) and facial expression (70%).
- Scoring: 20 points per correct answer → max 100.
- After 5 questions: modal shows correct answers, confidence score, interview score, and wrong answers with corrections.

### Premium Features (Text-based & Voice-based)

#### Text-based Premium
- User can set any language, any position, difficulty (Easy/Medium/Hard), and number of questions (1‑50).
- Questions are generated dynamically by Groq AI (no pre‑stored questions).
- Same webcam confidence and gesture support.
- Scoring: each correct answer gives 1 point; final score = (correct / total) * 100.

#### Voice-based Premium
- User speaks answers instead of selecting options.
- Speech is transcribed using Groq Whisper (supports 100+ languages, including Myanmar, Chinese, Japanese, etc.).
- Answer evaluation by Groq:
  - Perfect match → 1 point
  - Partially correct / close → 0.5 point (feedback “Almost there!”)
  - Wrong → 0 point
- Confidence score combines face metrics (70%) with voice volume (30%).
- Final score = (total points / total questions) * 100.
- “Show Question” button hides the question until user wants to see it.
- “Listen Question” button reads the question aloud using browser TTS (fallback to text if voice not available).

### Admin Dashboard
- View all registered users.
- Manage positions (add/edit/delete).
- Add new questions for any position (English/Myanmar, any difficulty).
- Approve or reject premium requests.
- Update pricing plans.

## Scoring & Confidence – Detailed Explanation

### Free Version (Text)
- **Score** = correct_count × 20 (max 100)
- **Confidence** = (EyeContactScore × 0.3) + (ExpressionScore × 0.7)  
  ExpressionScore: happy=95, neutral=60, surprised=45, fearful/angry/disgusted=20, sad=10

### Premium Text-based
- **Score** = (correct_count / total_questions) × 100  
- **Confidence** same as free version (webcam only)

### Premium Voice-based
- **Points per question**: perfect=1, suggest=0.5, wrong=0  
- **Score** = (total_points / total_questions) × 100  
- **Confidence** = (FaceConfidence × 0.7) + (VoiceVolume × 0.3)  
  FaceConfidence = same as free version  
  VoiceVolume = average recorded volume (0‑100)

## Technology Stack

- **Backend**: Python 3.11, Flask, PyMySQL, Flask-Mail, Groq API
- **Frontend**: HTML5, CSS3, JavaScript, face-api.js, MediaPipe Hands, WebRTC
- **Database**: MySQL

## Installation & Setup

1. Clone repository: `git clone <url>`
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Create `config.py` (see sample below).
6. Run MySQL and create database (automatically on first run).
7. Run `python app.py` and open `http://localhost:5000`.

### Sample config.py
```python
class Config:
    SECRET_KEY = 'your-secret-key'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'interview_practice_db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your-email@gmail.com'
    MAIL_PASSWORD = 'your-app-password'
    MAIL_DEFAULT_SENDER = 'your-email@gmail.com'
    GROQ_API_KEY = 'your-groq-api-key'
    GROQ_MODEL = 'llama-3.3-70b-versatile'
