from backend.prompts import ROLE_PROMPTS
import random

def ask_question(role: str):
    questions = ROLE_PROMPTS.get(role.lower(), ROLE_PROMPTS["python"])
    return random.choice(questions)
