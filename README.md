🧠 AI Interview Simulator

An AI-powered interview practice platform that evaluates candidate answers using semantic similarity scoring and dynamically adapts question difficulty in real time.
---

🚀 Live Demo

🔗 Frontend App:
https://ai-interview-frontend-39id.onrender.com

🔗 Backend API Docs:
https://ai-interview-simulator-u1mb.onrender.com/docs
---


🎯 Key Features

✅ AI-based answer evaluation
✅ Semantic similarity scoring (TF-IDF + Cosine Similarity)
✅ Automatic score generation (0–10 scale)
✅ Intelligent feedback system
✅ Adaptive follow-up question generation
✅ Dynamic difficulty progression (Easy → Medium → Hard)
✅ Full-stack architecture (FastAPI + Streamlit)
✅ Cloud deployment on Render
---


🏗 System Architecture
User (Frontend - Streamlit)
        ↓
API Call (Requests)
        ↓
Backend (FastAPI)
        ↓
NLP Evaluation (TF-IDF + Cosine Similarity)
        ↓
Score + Feedback + Next Question
        ↓
Response to Frontend
---


🧠 How It Works

-User submits an interview answer.
-Backend compares the answer with a predefined ideal response.
-TF-IDF vectorization converts text into numerical feature vectors.
-Cosine similarity measures semantic closeness.
-Similarity score is converted to a 0–10 interview score.
-Based on performance, a new question is generated at an appropriate difficulty level.
---


📊 Scoring Logic

Similarity Score	Difficulty Level
≥ 8	(Hard)
5 – 7.9	(Medium)
< 5	(Easy)
---


🛠 Tech Stack

🔹 Backend
 FastAPI
 Scikit-learn
 Uvicorn
🔹 Frontend
 Streamlit
 Requests
🔹 NLP
 TF-IDF Vectorization
 Cosine Similarity
🔹 Deployment
 Render (Cloud Hosting)
---


📂 Project Structure

ai-interview-simulator/
│
├── backend/
│   ├── main.py
│   ├── scoring.py
│   ├── prompts.py
│   └── __init__.py
│
├── frontend/
│   └── app.py
│
├── requirements.txt
└── README.md
---


💡 Future Enhancements

-Role-based interviews (ML / Backend / Data Science)
-Resume-based personalized interview generation
-Voice-enabled interview mode
-GPT-based answer evaluation
-Interview history tracking & analytics dashboard
---


👩‍💻 Author

Anusha K A
Aspiring AI Engineer | Data Science Student
Passionate about building real-world AI systems 🚀


