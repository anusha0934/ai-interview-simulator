from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
from backend.prompts import IDEAL_ANSWERS, QUESTION_BANK




vectorizer = TfidfVectorizer()

def evaluate_answer(question: str, user_answer: str):
    ideal_answer = IDEAL_ANSWERS.get(question)

    if not ideal_answer:
        return 5, "No reference answer available."

    texts = [user_answer, ideal_answer]
    vectors = vectorizer.fit_transform(texts)

    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    score = round(similarity * 10, 1)

    if score >= 8:
        feedback = "Excellent answer with strong understanding."
    elif score >= 5:
        feedback = "Good answer, but could be improved with examples."
    else:
        feedback = "Answer needs more clarity and key concepts."

    return score, feedback


def get_followup_question(score: float):
    if score >= 8:
        level = "hard"
    elif score >= 5:
        level = "medium"
    else:
        level = "easy"

    question = random.choice(QUESTION_BANK[level])
    return level, question
