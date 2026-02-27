# AI Resume Analyzer & Semantic Job Matcher

An AI-powered web application that analyzes resumes and recommends suitable job roles using Natural Language Processing.

## 🚀 Features
- Semantic job matching using TF-IDF & cosine similarity
- PDF text extraction
- OCR support for image-based resumes
- REST API built with FastAPI
- Interactive frontend built with Streamlit
- Resume strength score visualization

## 🛠 Tech Stack
- Python
- FastAPI
- Streamlit
- Scikit-learn
- Tesseract OCR

## 📊 How It Works
1. Upload Resume (PDF)
2. Extract text (pdfplumber / OCR)
3. Convert text to TF-IDF vectors
4. Compute cosine similarity
5. Rank job roles by match percentage

## 🔮 Future Scope
- Transformer-based semantic embeddings
- Cloud deployment
- Skill-gap analysis
- User authentication system