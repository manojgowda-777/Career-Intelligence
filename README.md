
# Career Intelligence 🚀

### AI-Powered Career Intelligence & Job-Market Skill Assessment Platform

Career Intelligence is a platform designed to help students and job seekers understand current job-market requirements, evaluate their skills, identify skill gaps, and improve their career readiness.

The platform collects job-market information, extracts in-demand skills, compares them with user skills and resumes, and provides insights to help users prepare for their target roles.

---

## 🎯 Project Objectives

- Understand the skills required for different job roles.
- Analyze current job-market skill demand.
- Compare user skills with industry requirements.
- Identify missing skills and skill gaps.
- Evaluate career readiness through assessments.
- Analyze GitHub profiles to understand technical skills.
- Help users make better career-learning decisions.

---

## ✨ Key Features

### 1. Search Your Role
- Search for a target job role.
- Collect relevant job-market information.
- Extract skills required for the selected role.
- Analyze the demand for different skills.

### 2. Search Jobs
- Search for available job opportunities.
- Retrieve job postings from external job sources.
- View relevant job information and application links.

### 3. Resume Analyzer
- Upload a resume in PDF format.
- Extract skills from the resume.
- Compare resume skills with job-market requirements.
- Identify missing skills and improvement areas.

### 4. MCQ Assessment
- Generate multiple-choice questions.
- Test technical knowledge.
- Submit answers and evaluate performance.

### 5. GitHub Analyzer
- Analyze a user's GitHub profile.
- Retrieve relevant GitHub information.
- Evaluate technical skills using a scoring system.

---

## 🛠️ Technologies Used

### Frontend
- Next.js
- React.js
- JavaScript
- Tailwind CSS

### Backend
- Python
- Flask

### Data Processing & Machine Learning
- Pandas
- NumPy
- Scikit-learn
- Python-based skill extraction and analysis

### Data Collection
- Himalayas.app job data source
- Python-based data collection and preprocessing

### GitHub Integration
- GitHub API

### Development Tools
- Visual Studio Code
- Git
- GitHub

---

## 📂 Project Structure

```text
Career Intelligence/
│
├── backend/
│   ├── app.py
│   ├── mcq_engine.py
│   ├── mcq_questions.py
│   ├── resume_analyzer.py
│   └── skill_library.py
│
├── data-collector/
│   ├── job_collector.py
│   ├── job_preprocessor.py
│   ├── run_pipeline.py
│   └── skill_extractor.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── GitHub Analyzer/
│   ├── github_api.py
│   ├── github_client.py
│   └── scoring.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── README.md
│
└── .gitignore
```

---

## ⚙️ Installation and Setup

### Prerequisites

Make sure the following are installed:

- Python
- Node.js and npm
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/manojgowda-777/Career-Intelligence.git
```

### 2. Open the Project

```bash
cd Career-Intelligence
```

### 3. Setup the Frontend

```bash
cd frontend
npm install
```

Start the frontend:

```bash
npm run dev
```

Frontend runs at:

```text
http://localhost:3000
```

### 4. Setup the Python Backend

Open another terminal from the project root.

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the required Python packages using your backend dependency file or install the required packages individually.

Start the Flask backend:

```bash
cd backend
python app.py
```

The main backend runs at:

```text
http://127.0.0.1:5000
```

**Note:** Configure the required environment variables and API keys locally before running the application. Never upload secret keys to GitHub.

---

## 🔄 How It Works

1. The user selects or searches for a target job role.
2. The system collects relevant job-market information.
3. Job descriptions are processed to extract required skills.
4. The platform analyzes skill demand.
5. Users can upload their resumes or take assessments.
6. The system compares user skills with job requirements.
7. Skill gaps and career-readiness insights are presented.

---

## 🔮 Future Improvements

- Improve skill extraction accuracy.
- Expand job-market data sources.
- Enhance career-readiness scoring.
- Provide personalized learning recommendations.
- Improve resume analysis and skill matching.
- Add more job roles and technical assessments.

---

## 👨‍💻 Developer

**Manoj S**

Computer Science and Design

---

## 📌 Project Status

Developed as a placement-oriented career intelligence project.

---

## ⭐ Support

If you find this project useful, consider giving the repository a star!
