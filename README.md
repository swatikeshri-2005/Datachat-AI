# 🚀 DataChat AI – Chat with Any CSV

DataChat AI is an AI-powered data analysis platform that allows users to upload CSV datasets and interact with them using natural language. The application combines Retrieval-Augmented Generation (RAG), vector search, and local Large Language Models (LLMs) to provide intelligent answers from structured data.

---

## ✨ Features

* 📁 Upload any CSV file
* 🤖 Chat with your data using natural language
* 🔍 Semantic search using FAISS Vector Database
* 🧠 Local LLM support using Ollama (Llama 3.2)
* 📊 Automatic dataset insights
* ⚡ FastAPI backend
* 🎨 React + Vite frontend (optional)
* 🔒 Runs completely offline

---

## 🏗️ Project Architecture

```text
                ┌──────────────┐
                │ CSV Upload   │
                └──────┬───────┘
                       │
                       ▼
               ┌───────────────┐
               │ Pandas Loader │
               └──────┬────────┘
                      │
                      ▼
            ┌──────────────────┐
            │ Document Builder │
            └────────┬─────────┘
                     │
                     ▼
            ┌──────────────────┐
            │ Embeddings Model │
            └────────┬─────────┘
                     │
                     ▼
            ┌──────────────────┐
            │  FAISS Vector DB │
            └────────┬─────────┘
                     │
                     ▼
              User Question
                     │
                     ▼
            Similarity Search
                     │
                     ▼
              Llama 3.2 (Ollama)
                     │
                     ▼
                 AI Response
```

---

## 📂 Project Structure

```text
DataChat-AI/
│
├── backend/
│   ├── main.py
│   ├── csv_loader.py
│   ├── vector_store.py
│   ├── chat_engine.py
│   ├── insights.py
│   ├── charts.py
│   ├── requirements.txt
│   ├── uploads/
│   └── vector_db/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── App.jsx
│   └── package.json
│
├── README.md
└── .gitignore
```

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* Python
* Pandas
* NumPy

### AI & RAG

* LangChain
* Ollama
* Llama 3.2
* Sentence Transformers
* FAISS

### Frontend

* React
* Vite
* Axios

### Visualization

* Plotly
* Matplotlib

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/DataChat-AI.git

cd DataChat-AI
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
cd backend

pip install -r requirements.txt
```

---

## 🤖 Install Ollama

Download and install Ollama:

https://ollama.com

Pull Llama 3.2:

```bash
ollama pull llama3.2
```

Test:

```bash
ollama run llama3.2
```

---

## ▶️ Run Backend

```bash
cd backend

uvicorn main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger API:

```text
http://127.0.0.1:8000/docs
```

---

## 📤 Upload Dataset

Endpoint:

```http
POST /upload
```

Upload any CSV file.

Example:

```csv
id,name,department,salary
1,John,IT,50000
2,Alice,HR,45000
3,Bob,Finance,60000
```

---

## 💬 Chat with Dataset

Endpoint:

```http
POST /chat
```

Request:

```json
{
  "question": "Who works in HR?"
}
```

Response:

```json
{
  "answer": "Alice works in HR."
}
```

---

## 📊 Generate Insights

Endpoint:

```http
GET /insights
```

Example Response:

```json
{
  "insights": [
    "Rows: 891",
    "Columns: 12",
    "Age: Average = 29.70",
    "Fare: Average = 32.20"
  ]
}
```

---

## 🧪 Testing with Titanic Dataset

Example Questions:

```text
Who was passenger 1?

What is the fare of passenger 10?

Which passengers were in first class?

Show details of female passengers.

Which passenger paid the highest fare?
```

---

## 🔮 Future Improvements

* Multi-file CSV support
* Pandas DataFrame Agent
* SQL Query Generation
* Automatic Chart Generation
* Dashboard Analytics
* PDF Report Export
* User Authentication
* Chat Memory
* Docker Deployment

---

## 📌 Resume Description

Developed an AI-powered CSV analytics platform using FastAPI, LangChain, FAISS, and Ollama (Llama 3.2). Implemented Retrieval-Augmented Generation (RAG) for semantic search over structured datasets, enabling natural language querying, automated insights generation, and intelligent data exploration through a conversational interface.

---

## 👨‍💻 Author

Swati Keshri

AI/ML Enthusiast | Data Science | Generative AI | Full Stack AI Applications
