import streamlit as st
from huggingface_hub import InferenceClient
import pdfplumber

# Your Hugging Face access token
HF_TOKEN=st.secrets["HF_TOKEN"]
MODEL_ID=st.secrets["MODEL_ID"]
client = InferenceClient(model=MODEL_ID, token=HF_TOKEN)

# System prompt for resume/interview coaching
SYSTEM_PROMPT = """
You are a career assistant named 'NaukriMitra' who helps Indian users write better resumes and prepare for interviews.
Always respond respectfully and clearly, in English based on the user's input.
Give suggestions on improving resumes for ATS, offer feedback with 1–5 stars, and simulate mock interviews when asked.
"""
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()
def generate_reply(prompt):
    response = client.chat_completion(
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7
    )
    return response.choices[0].message["content"]



st.set_page_config(page_title="Resume & Interview Coach", layout="centered")
st.title("📄 Resume Analyzer + 🧠 Interview Coach")
st.markdown("Built with **Meta LLaMA 3** on Hugging Face 🤖")

tab1, tab2 = st.tabs(["📄 Resume Feedback", "🎤 Interview Coach"])

with tab1:
    uploaded = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
    if uploaded:
        if uploaded.type == "application/pdf":
            resume_text = extract_text_from_pdf(uploaded)
        else:
            resume_text = uploaded.read().decode("utf-8", errors="ignore")
        
        st.text_area("Resume Content", resume_text, height=300)
        
        if st.button("Analyze Resume"):
            with st.spinner("Analyzing..."):
                reply = generate_reply(f"Please analyze and give feedback for the following resume:\n{resume_text}")
                st.success("Feedback:")
                st.write(reply)

with tab2:
    role = st.text_input("Job Role for Interview:")
    question = st.text_area("Ask a question or say 'Start mock interview'")
    if st.button("Get Interview Help"):
        with st.spinner("Thinking..."):
            full_prompt = f"I am preparing for an interview as a {role}. {question}"
            reply = generate_reply(full_prompt)
            st.success("Assistant:")
            st.write(reply)
