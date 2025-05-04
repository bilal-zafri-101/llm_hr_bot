## 🧠 LLM-Powered HR Bot

An AI-powered tool that automates HR workflows like **resume parsing**, **job description matching**, and **candidate screening** using **Large Language Models (LLMs)**, **FAISS**, and **Streamlit**.

---

### 🚀 Features

- ✅ Resume Parser (extracts candidate skills, education, experience)
- ✅ JD Parser & Embedding
- ✅ Candidate-to-JD Matching (using Sentence Transformers + FAISS)
- ✅ Streamlit UI for uploading resumes and job descriptions
- ✅ Extensible & Lightweight project structure
- ✅ Git & Virtual Environment support

---

### 📁 Project Structure
```
llm_hr_bot/
│
├── app.py                     # Streamlit frontend
├── .gitignore
├── requirements.txt
├── README.md
│
├── examples/   # Uploaded JDs and Resumes
│
├── utils/
│   ├── resume_parser.py       # Extracts info from resumes
│   ├── jd_parser.py           # Parses JDs + embeddings
│   └── matcher.py             # FAISS-based matcher
```

---

### ⚙️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/bilal-zafri-101/llm_hr_bot.git
cd llm_hr_bot
```

2. **Create and activate a virtual environment**
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the app**
```bash
streamlit run app.py
```

---

### 🧩 Tech Stack

- 🔤 **OpenAI / LLMs / Sentence Transformers**
- 🔍 **FAISS** for similarity search
- 🎛️ **Streamlit** for UI
- 🧰 **Python, Pandas, Regex, OS, JSON**
- 🔗 **Git** for version control

---

### 💡 Future Ideas

- 🧑‍💼 Candidate Ranking System  
- 📩 Email Automation for Interview Scheduling  
- 🗣️ LLM-Powered Interview Questions Generator  
- 🔒 Admin Login Panel

---

### 📬 Contact

**Built with ❤️ by [Your Name]**  
📧 Email: bilal.zafri.work@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/bilalzafri/) 