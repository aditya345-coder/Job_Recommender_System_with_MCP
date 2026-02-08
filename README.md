Here is a professional, clean, and **easy-to-understand** `README.md` for your project.

I have written this specifically to appeal to recruiters—it highlights **what** the project does and **why** your engineering choices (like LangGraph and Fallback LLMs) are smart, without using overly complex jargon.

***

### Instructions
1.  Create a file named `README.md` in your main folder.
2.  Paste the code below into it.
3.  **Important:** Take a screenshot of your Streamlit app running, name it `demo.png`, create a folder named `images`, and put the picture there.

***

```markdown
# 🤖 AI Job Intelligence & Resume Matching System

**A smart career assistant that doesn't just "search" for jobs—it understands your resume, finds the perfect roles, and explains *why* you are a match.**

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![LangGraph](https://img.shields.io/badge/AI_Orchestration-LangGraph-orange)
![MCP](https://img.shields.io/badge/Protocol-MCP-green)

---

## 📖 The Problem
Traditional job boards are dumb. They look for keyword matches. If you are a "Python Developer" but the job asks for a "Backend Engineer," you might be missed.

## 💡 The Solution
This project is an **Intelligence System**. It reads your PDF resume like a human recruiter would:
1.  **Extracts** your actual skills (technical & soft).
2.  **Infers** what job titles you are actually qualified for.
3.  **Scrapes** real-time jobs from LinkedIn/Naukri (or uses mock data for testing).
4.  **Matches** you based on logic, not just keywords.
5.  **Explains** the match: "You are an 85% match because you know React, but you need to learn Docker."

---

## ⚙️ Tech Stack

*   **Frontend:** Streamlit (Clean, responsive UI)
*   **AI Logic:** LangGraph (State-based multi-step reasoning)
*   **LLMs:** Hybrid system (Google Gemini, Hugging Face, OpenAI) with automatic fallback.
*   **Data Fetching:** Apify Client (Real-time scraping) & Threading (Concurrent execution).
*   **Agent Protocol:** MCP (Model Context Protocol) server included.

---

## 🚀 How It Works (The "Secret Sauce")

This isn't just a script; it's a **State Machine**.

1.  **Smart LLM Switching:** The system prioritizes **Free/Fast models** (Google Gemini). If they fail or hit rate limits, it automatically switches to **OpenAI** or **Hugging Face** so the app never crashes.
2.  **Hybrid Matching:** It uses math (Set Theory) to calculate the score instantly and AI only for the explanation. This makes it fast and cheap to run.
3.  **Pluggable Data:**
    *   *Demo Mode:* Uses instant local JSON data (great for testing).
    *   *Live Mode:* If you add an `APIFY_API_TOKEN`, it scrapes real live jobs from the web.

---

## 🛠️ Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/aditya345-coder/Job_Recommender_System_with_MCP.git
cd job-recommender
```

**2. Create a Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up API Keys**
Create a file named `.env` and add your keys (you only need one to start!):
```env
# Primary LLM (Free Tier available)
GOOGLE_API_KEY="your_gemini_key"

# Backup LLM (Optional)
OPENAI_API_KEY="your_openai_key"

# For Real-Time Scraping (Optional - App uses Mock Data if missing)
APIFY_API_TOKEN="your_apify_key"
```

**5. Run the App**
```bash
streamlit run app.py
```

---

## 🧠 Model Context Protocol (MCP)

This project includes an **MCP Server** (`mcp_server.py`). This allows AI Agents (like Claude Desktop or custom bots) to use this project as a tool.

To run the MCP server:
```bash
python mcp_server.py
```
*Your AI agent can now "read resumes" and "fetch jobs" using this backend!*

---

## 📸 Demo

