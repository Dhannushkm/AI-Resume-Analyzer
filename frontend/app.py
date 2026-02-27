import streamlit as st
import requests

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Header Section
# -----------------------------
st.title("📄 AI Resume Analyzer & Job Matcher")
with st.sidebar:
    st.header("About This System")
    st.write(
        "This AI-powered system analyzes resumes using "
        "TF-IDF vectorization and cosine similarity "
        "to recommend job roles based on semantic matching."
    )
st.markdown("Upload your resume and get AI-powered job recommendations.")

st.divider()

# -----------------------------
# File Upload Section
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF only)",
    type=["pdf"]
)

# -----------------------------
# Placeholder for Results
# -----------------------------
# -----------------------------
# Results Section
# -----------------------------
if uploaded_file is not None:

    st.info("Analyzing resume...")

    files = {
        "file": (uploaded_file.name, uploaded_file, "application/pdf")
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/analyze",
            files=files
        )

        if response.status_code == 200:
            data = response.json()

            st.success("Analysis Complete!")

            # -------- Skills Section --------
            st.markdown("### 🧠 Analysis Summary")

            if data["skills"]:
               st.write(
        f"The resume demonstrates strengths in {', '.join(data['skills'])}. "
        "Based on semantic similarity, the system recommends roles ranked above."
    )
            else:
                st.write( "The system could not identify strong domain-specific skills. "
        "Consider adding technical keywords and measurable achievements.")

            # -------- Job Section --------
            st.subheader("📊 Job Recommendations")

            if data["job_ranking"]:
                top_job = data["job_ranking"][0]
                st.markdown("### 📈 Resume Strength Score")

                strength_score = top_job["score"]

                if strength_score >= 70:
                    st.success(f"Excellent Match Potential — {strength_score}%")
                elif strength_score >= 40:
                    st.warning(f"Moderate Match Potential — {strength_score}%")
                else:
                    st.error(f"Low Match Potential — {strength_score}%")

                    st.progress(min(strength_score / 100, 1.0))


                st.markdown("### 🏆 Top Recommendation")
                st.success(f"{top_job['title']} — {top_job['score']}% match")

                st.divider()

                st.markdown("### 📌 All Matches")

                for job in data["job_ranking"]:
                    score = job["score"]

                    col1, col2 = st.columns([3, 1])

                    with col1:
                        st.write(f"**{job['title']}**")

                    with col2:
                        if score >= 60:
                            st.markdown(f"<span style='color:green'>{score}%</span>", unsafe_allow_html=True)
                        elif score >= 30:
                            st.markdown(f"<span style='color:orange'>{score}%</span>", unsafe_allow_html=True)
                        else:
                            st.markdown(f"<span style='color:red'>{score}%</span>", unsafe_allow_html=True)

                            st.progress(min(score / 100, 1.0))

        else:
            st.error("Error in backend response.")

    except Exception as e:
        st.error("Could not connect to backend.")
        st.write(e)
