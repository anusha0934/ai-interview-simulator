from fastapi import FastAPI
from pydantic import BaseModel
from scoring import evaluate_answer, get_followup_question


app = FastAPI(title="AI Interview Simulator")

class InterviewAnswer(BaseModel):
    question: str
    answer: str


@app.post("/ask")
def evaluate(data: InterviewAnswer):
    score, feedback = evaluate_answer(
        question=data.question,
        user_answer=data.answer
    )

    level, followup_question = get_followup_question(score)

    return {
        "question": data.question,
        "answer": data.answer,
        "score": score,
        "feedback": feedback,
        "next_level": level,
        "followup_question": followup_question
    }


