import streamlit as st
import PyPDF2
import spacy
import plotly.graph_objects as go

# ---------------- NLP ----------------
nlp = spacy.load("en_core_web_sm")

SKILLS = [
    "python", "java", "c++", "machine learning",
    "data analysis", "sql", "html", "css", "javascript"
]

# ---------------- FUNCTIONS ----------------
def extract_text_from_pdf(file):
    text = ""
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted
    return text

def extract_skills(text):
    doc = nlp(text.lower())
    return list(set([token.text for token in doc if token.text in SKILLS]))

def calculate_ats_score(resume_skills, job_skills):
    if len(job_skills) == 0:
        return 0
    return round((len(set(resume_skills) & set(job_skills)) / len(job_skills)) * 100, 2)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #3a0ca3, #7209b7, #4361ee);
    padding: 70px;
    border-radius: 0 0 50px 50px;
    text-align: center;
    color: white;
}
.card {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("""
<div class="hero">
    <h1>🚀 AI Resume Analyzer</h1>
    <h3>Get expert feedback on your resume instantly</h3>
    <p>AI-powered ATS resume checker</p>
    <p><b>Made by Mitansh 💻</b></p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- INPUT ----------------
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("📄 Upload Resume", type=["pdf"])

with col2:
    job_desc = st.text_area("💼 Job Description")

# ---------------- BUTTON ----------------
if st.button("🚀 Analyze Resume"):

    if uploaded_file:

        with st.spinner("Analyzing..."):
            text = extract_text_from_pdf(uploaded_file)

            resume_skills = extract_skills(text)
            job_skills = extract_skills(job_desc)

            score = calculate_ats_score(resume_skills, job_skills)
            missing = list(set(job_skills) - set(resume_skills))

        st.success("Analysis Complete ✅")

        # ---------------- RESULT ----------------
        st.markdown("## 📊 Results")

        # BIG SCORE
        st.markdown(f"""
        <div style="text-align:center; padding:20px;">
            <h1 style="color:#00ffcc;">{score}%</h1>
            <p>ATS Score</p>
        </div>
        """, unsafe_allow_html=True)

        st.progress(score / 100)

        # CHART
        fig = go.Figure(data=[go.Pie(
            labels=['Score', 'Remaining'],
            values=[score, 100-score],
            hole=0.6
        )])

        fig.update_layout(showlegend=False, height=300)
        st.plotly_chart(fig)

        # SKILLS + MISSING
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🧠 Skills")

            skills_html = ""
            for skill in resume_skills:
                skills_html += f"<span style='background:#4361ee; color:white; padding:8px 12px; border-radius:10px; margin:5px; display:inline-block;'>{skill}</span>"

            st.markdown(skills_html, unsafe_allow_html=True)

        with col2:
            st.subheader("⚠️ Missing Skills")

            missing_html = ""
            for skill in missing:
                missing_html += f"<span style='background:#ff4d4d; color:white; padding:8px 12px; border-radius:10px; margin:5px; display:inline-block;'>{skill}</span>"

            st.markdown(missing_html if missing else "🎉 No missing skills!", unsafe_allow_html=True)

    else:
        st.warning("Please upload resume ⚠️")
