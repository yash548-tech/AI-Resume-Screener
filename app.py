import streamlit as st
import PyPDF2
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Resume Screener", page_icon="📄")

st.title("📄 Advanced AI Resume Screener")

st.write("Analyze your resume with AI")

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
    "Paste Job Description"
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

    st.subheader("✅ Detected Skills")

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

    # Chart
    st.subheader("📈 Skill Match Chart")

    labels = ['Matched Skills', 'Missing Skills']

    matched_count = len(matched_skills)
    missing_count = len(jd_skills) - len(matched_skills)

    values = [matched_count, missing_count]

    fig, ax = plt.subplots()

    ax.pie(values, labels=labels, autopct='%1.1f%%')

    st.pyplot(fig)

    # Missing Skills
    missing_skills = []

    for skill in jd_skills:
        if skill not in detected_skills:
            missing_skills.append(skill)

    st.subheader("❌ Missing Skills")

    if missing_skills:
        for skill in missing_skills:
            st.error(skill)

    else:
        st.success("No Missing Skills")

    # Smart AI Suggestions
    st.subheader("🤖 AI Suggestions")

    if match_score >= 80:
        st.success("Your resume is strong for this role.")

    elif match_score >= 50:
        st.warning("Add more relevant projects and skills.")

    else:
        st.error("Your resume needs improvement for this job.")

    if "projects" not in resume_text:
        st.warning("Add project section to improve resume strength.")

    if "internship" not in resume_text:
        st.warning("Add internship experience if available.")