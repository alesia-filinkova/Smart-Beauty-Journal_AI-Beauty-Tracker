# 🪞 Smart-Beauty-Journal_AI-Beauty-Tracker

**AI-powered personal beauty tracker for skincare and haircare**

Smart Beauty Journal is an end-to-end **AI application** that helps users track their skincare progress over time.
It uses **computer vision** to analyze skin condition, **LLMs** to provide personalized recommendations, and interactive **data visualization** to show real improvements.

---

## ✨ Features

* 📸 **Skin analysis with AI (YOLOv8 / CV)** – detect acne, dryness, or other conditions from uploaded photos
* 🔄 **Before/After comparison** – visualize skin progress over time
* 📊 **Interactive dashboards** – track improvements with charts (Plotly/D3.js)
* 💡 **AI skincare assistant (LLM + RAG)** – ask questions and get recommendations based on dermatology articles
* ⏰ **Reminders & predictions** – personalized notifications and improvement forecasts
* 📱 **Cross-platform UI** – mobile app (Flutter/React Native) + web client (Streamlit/Dash MVP)

---

## 🏗️ Tech Stack

**Frontend**

* Flutter / React Native (mobile)
* Streamlit / Dash (prototype web UI)

**Backend**

* Python + FastAPI (API Gateway)
* PostgreSQL (user data & skin logs)
* MinIO / AWS S3 (image storage)

**Machine Learning**

* YOLOv8 / EfficientNet (skin condition detection)
* SentenceTransformers + FAISS / Weaviate (vector DB)
* GPT-4 / LLaMA (AI-powered recommendations)

**Visualization**

* Plotly / D3.js (progress graphs & heatmaps)


---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/smart-beauty-journal.git
cd smart-beauty-journal
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run backend

```bash
uvicorn app.main:app --reload
```

### 4. (Optional) Run web UI prototype

```bash
streamlit run frontend/app.py
```

---

## 📊 Example Workflow

1. User uploads a skin photo
2. CV model analyzes acne count and skin features
3. Data is stored in PostgreSQL + progress chart is updated
4. User can compare “before/after” and ask AI for personalized tips
5. App sends reminders to keep skincare routine consistent

---

## 🎯 Project Goal

This project demonstrates **end-to-end ML engineering skills**:

* dataset preparation & model training,
* serving ML models with FastAPI,
* database & storage integration,
* LLM-powered recommendation engine,
* mobile & web integration for a real-world MVP.

---

## 💼 Resume Pitch

*“Built an AI-powered beauty tracker with computer vision (YOLOv8) for skin analysis, LLM-based recommendations with RAG, interactive visualizations (Plotly), and a mobile-first frontend. Designed and deployed a complete ML pipeline from data collection to real-time inference and user-facing UI.”*

---

✨ With Smart Beauty Journal, beauty meets AI.

