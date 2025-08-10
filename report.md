1.1. Team Information
Team Name: [Team zzz]

Team Members:

Member 1: [Dhanush Allenki] 



1.2. Application Overview
NaukriMitra is an AI-powered career assistant designed to help Indian job seekers bridge the gap between their resume and their dream job. The application tackles the critical challenge of resume optimization and interview preparation by providing personalized, actionable feedback.

The primary mission is to empower users by demystifying the recruitment process. For the one-week development sprint, the Minimum Viable Product (MVP) was scoped to deliver immediate value through three core functions:

Resume Parsing: Reliably extract text and structure from user-uploaded PDF resumes.

Job Description Analysis: Score the resume against a specific job description, highlighting missing keywords and suggesting improvements.

Personalized Interview Prep: Generate a list of tailored interview questions based directly on the user's resume and the target job's requirements.

1.3. AI Integration Details
NaukriMitra's intelligence is driven by a combination of precise text extraction and a powerful Large Language Model (LLM).

PDF Text Extraction: We use the pdfplumber library. It was chosen over other libraries for its robustness in accurately extracting text from various resume formats, preserving layout information which can be crucial for understanding document structure.

Core AI Model: The application's analytical capabilities are powered by Meta Llama 3, a state-of-the-art open-source LLM. Llama 3 was selected for its advanced reasoning, instruction-following capabilities, and strong performance in generating coherent, context-aware text.

Implementation (Prompt Engineering): The interaction with Llama 3 is managed through two carefully engineered prompts:

Resume Analysis Prompt: The extracted resume text and the user-pasted job description are fed into a detailed prompt. This prompt instructs the LLM to act as an expert HR recruiter, perform a comparative analysis, identify key strengths and weaknesses, and suggest specific, actionable improvements to make the resume more ATS-friendly and better aligned with the job description.

Interview Question Prompt: A second prompt uses the resume and job description to generate a diverse set of interview questions. It is instructed to create a mix of technical, behavioral ("Tell me about a time..."), and resume-specific questions ("Your resume mentions a project on X, can you elaborate?").

1.4. Technical Architecture & Development
The architecture was designed for rapid implementation and a seamless user experience.

Frontend Framework: Streamlit serves as the complete frontend. Its interactive widgets and simple, Python-based structure allowed us to build a responsive UI for file uploads and text input/output without requiring web development expertise.

Core Logic: The backend logic is written in Python. The workflow is as follows:

A user uploads their PDF resume using st.file_uploader.

The user pastes a job description into an st.text_area.

pdfplumber opens the PDF in memory and extracts all text.

The extracted text and job description are formatted into the predefined prompts.

The prompts are sent to the Llama 3 model via the transformers library.

The model's generated response (resume analysis and interview questions) is parsed and displayed back to the user in a clean, readable format using Streamlit components like st.markdown and st.expander.

Deployment Platform: The application is designed for deployment on Hugging Face Spaces, which provides native support for Streamlit and the necessary environment to run LLM inference.

1.5. User Testing & Feedback (Week 2 Plan)
Our Week 2 testing phase is focused on validating the quality and relevance of the AI-generated feedback.

Methodology:

Recruitment: We will target a group of 10-15 beta testers, primarily final-year university students and recent graduates who are actively applying for jobs. This group represents our core user demographic.

Task-Based Testing: Testers will be asked to use their own resume and find a real job description they are interested in. They will perform the full analysis and interview preparation loop.

Feedback Collection: We will use a Google Form to collect structured feedback. Key questions will focus on:

The accuracy of the resume analysis.

The actionability of the suggested improvements.

The relevance and difficulty of the generated interview questions.

Overall user experience and clarity of the interface.

Iteration: The collected feedback will be analyzed to identify patterns (e.g., "the analysis is too generic," "the questions are too easy"). This will inform prompt refinement and UI adjustments to be implemented during the week.
