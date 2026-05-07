import streamlit as st
import PyPDF2

st.set_page_config(page_title="AI Resume Screener", page_icon="📄")

st.title("📄 AI Resume Screener")
st.write("Upload your resume and compare it with Job Description")

skills_list = [
    "python",
    "java",
    "c++",
    "machine learning",
    "data science",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "django",
    "flask"
]

uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description Here"
)

if uploaded_file is not None:

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    resume_text = ""

    for page in pdf_reader.pages:
        resume_text += page.extract_text()

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    detected_skills = []

    for skill in skills_list:
        if skill in resume_text:
            detected_skills.append(skill)

    st.subheader("✅ Detected Resume Skills")

    col1, col2 = st.columns(2)

    with col1:
        for skill in detected_skills:
            st.success(skill)

    jd_skills = []

    for skill in skills_list:
        if skill in job_description:
            jd_skills.append(skill)

    matched_skills = []

    for skill in jd_skills:
        if skill in detected_skills:
            matched_skills.append(skill)

    if len(jd_skills) > 0:
        match_score = int((len(matched_skills) / len(jd_skills)) * 100)
    else:
        match_score = 0

    st.subheader("📊 Resume Match Score")

    st.progress(match_score / 100)

    if match_score >= 80:
        st.success(f"Excellent Match: {match_score}%")

    elif match_score >= 50:
        st.warning(f"Good Match: {match_score}%")

    else:
        st.error(f"Low Match: {match_score}%")

    missing_skills = []

    for skill in jd_skills:
        if skill not in detected_skills:
            missing_skills.append(skill)

    st.subheader("❌ Missing Skills")

    if missing_skills:
        for skill in missing_skills:
            st.error(skill)

    else:
        st.success("No Missing Skills 🎉")