# 🚀 AI Resume Analyzer

AI Resume Analyzer is a web-based application built using **Streamlit** and **Natural Language Processing (NLP)** techniques. It allows users to upload their resume and compare it with a job description to evaluate its effectiveness and ATS compatibility.

---

## 🎯 Features

- 📄 Extracts text from PDF resumes  
- 🧠 Identifies technical skills using NLP (spaCy)  
- 📊 Calculates ATS (Applicant Tracking System) score  
- ⚠️ Highlights missing skills based on job description  
- 💡 Provides improvement suggestions  
- 📈 Visualizes score using interactive charts  

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **spaCy (NLP)**
- **PyPDF2 (PDF Processing)**
- **Plotly (Data Visualization)**

---

## ⚙️ How It Works

1. Upload your resume (PDF format)
2. Paste a job description
3. The system extracts skills using NLP
4. Compares resume with job requirements
5. Displays:
   - ATS Score
   - Resume Skills
   - Missing Skills
   - Suggestions

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app_streamlit.py
