# Multi-Agent Backend

Backend service for the Multi-Agent system built with **Python**.
This backend powers the **AI agent orchestration using LangChain** and provides APIs used by the **Next.js Progressive Web App (PWA) frontend**.

## Tech Stack

* Python
* FastAPI
* LangChain
* AI Agents
* REST APIs
* Docker
* Async Processing

## Features

* 🤖 **Multi-agent system powered by LangChain**
* ⚡ High-performance APIs built with FastAPI
* 🔗 API layer for the **Next.js PWA frontend**
* 🧠 Agent orchestration and task execution
* 🔌 Integration with LLMs and external tools
* 📦 Modular and scalable backend architecture
* 🐳 Docker-ready deployment

## Architecture Overview

The backend manages agent orchestration and processes requests coming from the PWA frontend.

```id="fw72m1"
Next.js Frontend (PWA)
        │
        │ API Requests
        ▼
Python Backend (FastAPI)
        │
        ▼
LangChain Agent System
        │
        ▼
LLM / Tools / External APIs
```

## Project Structure

```id="ruok7s"
multi-agent-backend
│
├── app/                # Core backend application
├── agents/             # LangChain agent implementations
├── routes/             # API routes
├── services/           # Business logic
├── config/             # Configuration
├── utils/              # Helper functions
├── requirements.txt
└── main.py             # Entry point
```

## Installation

### 1. Clone Repository

```id="s82s7q"
git clone https://github.com/bipingithubtech/multi-agent-backend.git
cd multi-agent-backend
```

### 2. Create Virtual Environment

Windows

```id="vpa3r3"
python -m venv venv
venv\Scripts\activate
```

Mac/Linux

```id="5qgj7p"
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```id="9ytj5e"
pip install -r requirements.txt
```

## Run the Server

```id="n6ap2r"
python main.py
```

or

```id="9o6xsy"
uvicorn main:app --reload
```

Server runs at:

```id="e6np5n"
http://localhost:8000
```





ReDoc

```id="dquyo2"
http://localhost:8000/redoc
```

## Docker Setup

Build image

```id="v04kmk"
docker build -t multi-agent-backend .
```

Run container

```id="9rjfyq"
docker run -p 8000:8000 multi-agent-backend
```

## Frontend (PWA)

This backend powers the **Next.js Progressive Web App frontend**.

Frontend Repository:

```id="h0jbs8"
https://github.com/bipingithubtech/multi-agent-frontend
```



