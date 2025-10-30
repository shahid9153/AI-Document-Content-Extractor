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

## 📁 Project Structure

📁 Smart-AI-Document-Extractor/
│
├── app.py # Main Streamlit application file

├── .env # Environment variable file (contains API key)

├── requirements.txt # Python dependencies

└── README.md # Project documentation


---

⚙️ Installation & Setup

 ###1️⃣ Clone the Repository
bash
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
streamlit run app.py ```



🧠 How It Works

Load & Parse → The app loads the PDF using LangChain’s PyPDFLoader.

Extract Topics → Detects major headings using regex and builds topic-based sections.

Vectorization → (Optional for RAG) Converts document chunks into vector embeddings via FAISS.

AI Summarization → Sends extracted text to Gemini 2.5 Flash for concise summarization.

UI Display → Streamlit presents extracted content and summaries in a clean layout.

📘 Smart AI Document Content Extractor
────────────────────────────────────
✅ PDF processed successfully with 10 topics

📖 Extracted Topics:
1. INTRODUCTION
   → Discusses the background and importance of renewable energy.
2. METHODOLOGY
   → Explains data collection and analysis techniques.
...

✨ Summary:
This document explores the role of renewable energy in sustainable development. 
It outlines current challenges and proposes solutions focused on policy and innovation.

🚀 Future Enhancements

📊 Table and chart extraction

🗣️ Voice-based querying

🌐 Deployable version on Streamlit Cloud / Hugging Face Spaces

🧩 Multi-document support

💬 Chat memory for continuous Q&A

🧭 Quick Summary

✅ Upload → 🧠 Extract → ✨ Summarize → 📄 Understand — All in seconds!
Your smart companion for document understanding and summarization.

Developed by: Shahid Mulani
Powered by: LangChain · Gemini 2.5 Flash · Streamlit · FAISS · HuggingFace

🌟 If you found this project useful, please star ⭐ the repository to show your support!
