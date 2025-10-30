# 📘 Smart AI Document Content Extractor

> 🚀 An intelligent PDF document analysis tool powered by **Google Gemini 2.5 Flash** and **LangChain**.  
> Upload any PDF and instantly extract topics, summarize content, and explore key insights — all inside a clean Streamlit interface.

---

## 🧩 Overview

**Smart AI Document Content Extractor** is an advanced, AI-powered Streamlit app designed to understand your documents.  
It reads your PDFs, extracts structured content (topics and text), and generates smart summaries — making document comprehension effortless.

---

## 🎯 Features

| Feature | Description |
|----------|-------------|
| 📂 **PDF Upload** | Upload any PDF file directly from your system |
| 🧠 **Smart Extraction** | Automatically identifies section headings and extracts relevant content |
| 🧾 **AI Summarization** | Generates a detailed and easy-to-understand summary of the entire document |
| ⚡ **Gemini 2.5 Flash** | Uses Google’s latest **Gemini Flash model** for fast and accurate analysis |
| 🎨 **Modern UI** | Clean, elegant Streamlit-based design for a professional experience |
| 🔐 **Secure API Handling** | API key stored safely using `.env` environment variables |

---

## 🏗️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend/UI** | Streamlit |
| **LLM Model** | Google Gemini 2.5 Flash |
| **Framework** | LangChain |
| **Vector Store** | FAISS |
| **Embeddings** | HuggingFace Sentence Transformers |
| **Environment Management** | python-dotenv |
| **PDF Processing** | PyPDF via LangChain loaders |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/smart-ai-document-extractor.git
cd smart-ai-document-extractor

2️⃣ Create and Activate a Virtual Environment
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On macOS / Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Up Environment Variable

Create a .env file in your project root and add your Gemini API key:

GEMINI_API_KEY=your_gemini_flash_2_5_key_here

5️⃣ Run the App
streamlit run app.py



