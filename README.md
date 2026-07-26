# 🤖 CV Buddy AI

**An AI-powered Resume Builder & Career Coach built with Streamlit and Google Gemini AI.**

CV Buddy AI helps users create professional, ATS-friendly resumes through an interactive AI interview. Instead of filling out long forms, users simply chat with the AI, which gathers information, builds a resume, analyzes its quality, and allows exporting it in multiple formats.

---

## ✨ Features

### 🤖 AI Career Interview

* Interactive AI-powered resume interview
* Natural conversation flow
* Smart follow-up questions
* Automatic information extraction

### 📄 Resume Builder

* Live resume generation
* Professional resume formatting
* Real-time profile updates
* Automatic section organization

### 📊 ATS Resume Analyzer

* ATS compatibility score
* Resume completion percentage
* Strength analysis
* Improvement recommendations

### 💬 Smart Chat Manager

* Conversation history
* Context-aware responses
* Structured interview process
* Automatic profile updates

### 💾 Persistent Storage

* Automatic resume saving
* Conversation recovery
* Resume persistence after application restart

### 📤 Export Options

* PDF Resume
* TXT Resume

### 🛡️ Reliability

* Automatic retry on temporary API failures
* Multi-model Gemini fallback
* Graceful error handling

---

# 🖼️ Screenshots

> Add screenshots inside the `screenshots/` folder.

## Dashboard

```
screenshots/dashboard.png
```

## AI Interview

```
screenshots/chat.png
```

## Resume Preview

```
screenshots/resume.png
```

---

# 🏗️ Project Structure

```text
CV-Buddy-AI
│
├── app.py
├── core
│   ├── ai_engine.py
│   ├── ats_engine.py
│   ├── chat_manager.py
│   ├── interview_engine.py
│   ├── models.py
│   ├── pdf_generator.py
│   ├── profile_manager.py
│   ├── prompts.py
│   ├── resume_generator.py
│   ├── resume_preview.py
│   ├── session_manager.py
│   └── storage.py
│
├── data
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Elfadil94/CV-Buddy-AI.git
```

Enter the project directory:

```bash
cd CV-Buddy-AI
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Get your API key from Google AI Studio.

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 📋 Workflow

```text
User

↓

AI Interview

↓

Profile Extraction

↓

Resume Builder

↓

ATS Analysis

↓

Resume Preview

↓

PDF / TXT Export
```

---

# 🛠️ Technologies Used

* Python
* Streamlit
* Google Gemini AI
* ReportLab
* Python Dataclasses
* JSON Storage

---

# 🌟 Future Improvements

* DOCX Export
* Multiple Resume Templates
* AI Resume Optimization
* Job Description Matching
* LinkedIn Import
* Cloud Database
* User Authentication
* Multi-language Support

---

# 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

---

# 👨‍💻 Author

**Elfadil**

GitHub: https://github.com/Elfadil94

---

# ⭐ Support

If you found this project useful:

* ⭐ Star this repository
* 🍴 Fork the project
* 🐛 Report issues
* 💡 Suggest new features

Your support is greatly appreciated!
