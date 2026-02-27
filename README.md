# AI Resume Analyzer & Semantic Job Matcher

**An AI-powered web application that analyzes resumes and recommends suitable job roles using semantic NLP.**

---

## 🚀 Features

- 📄 Upload PDF resumes (text-based or image-based)
- 🧠 Intelligent semantic matching using TF-IDF and cosine similarity
- 🛠 OCR support for Canva & scanned resumes
- 🌐 REST API backend (FastAPI)
- 🖥 Frontend web UI (Streamlit)
- 📊 Ranked job recommendations with match scores

---

## 🧾 Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | Python, FastAPI, scikit-learn |
| Frontend | Streamlit |
| Text Parsing | pdfplumber, pytesseract, pdf2image |
| Machine Learning | TF-IDF (scikit-learn) |
| Deployment | Uvicorn |

---

## 🧠 How It Works

1. User uploads a resume (PDF)
2. Backend extracts text using pdfplumber
3. If no text layer, OCR converts pages to images using Tesseract
4. TF-IDF vectorizes resume and job descriptions
5. Cosine similarity compares vectors
6. Jobs are ranked by match percentage
7. Frontend displays results

---

## 📦 Installation (Local)

### 1. Clone repository
```bash
git clone https://github.com/Dhannushkm/AI-Resume-Analyzer.git

---

2. Create virtual environment
cd AI-Resume-Analyzer
python -m venv venv
venv\Scripts\activate

---

3. Install dependencies
pip install -r requirements.txt

---

4. Install Tesseract (Required for OCR)

Download from:
https://github.com/UB-Mannheim/tesseract/wiki

Add to PATH and note install location (e.g., C:\Program Files\Tesseract-OCR\tesseract.exe)

5. Install Poppler (Required by PDF2Image)

Download from:
https://github.com/oschwartz10612/poppler-windows/releases

Extract and note path.

---

▶️ Run Application
Backend:
cd backend
uvicorn main:app --reload
Frontend:
streamlit run frontend/app.py
