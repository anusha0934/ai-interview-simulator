import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(
    page_title="AI Interview Simulator",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 AI Interview Simulator")
st.caption("Practice interviews with AI-powered feedback")

question = st.text_input(
    "Interview Question",
    value="What is a Python decorator?"
)

answer = st.text_area(
    "Your Answer",
    height=150
)

if st.button("Evaluate Answer"):
    if answer.strip() == "":
        st.warning("Please enter an answer before submitting.")
    else:
        payload = {
            "question": question,
            "answer": answer
        }

        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()

            st.subheader("📊 Evaluation Result")
            st.metric("Score", f"{result['score']} / 10")

            if result["score"] >= 8:
                st.success(result["feedback"])
            elif result["score"] >= 5:
                st.info(result["feedback"])
            else:
                st.error(result["feedback"])
            st.subheader("🔁 Follow-up Question")
            st.write(result["followup_question"])
            st.caption(f"Difficulty level: {result['next_level'].upper()}")

        else:
            st.error("API Error. Please try again.")
    