# 📘 Smart AI Document Content Extractor Using RAG

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

**🧠 How It Works**

1] Load & Parse → The app loads the PDF using LangChain’s PyPDFLoader.

2] Extract Topics → Detects major headings using regex and builds topic-based sections.

3] Vectorization → (Optional for RAG) Converts document chunks into vector embeddings via FAISS.

4] AI Summarization → Sends extracted text to Gemini 2.5 Flash for concise summarization.

5] UI Display → Streamlit presents extracted content and summaries in a clean layout.

---

**✨ Summary:**
This document explores the role of renewable energy in sustainable development. 
It outlines current challenges and proposes solutions focused on policy and innovation.

🚀 Future Enhancements

📊 Table and chart extraction

🗣️ Voice-based querying

🌐 Deployable version on Streamlit Cloud / Hugging Face Spaces

🧩 Multi-document support

💬 Chat memory for continuous Q&A

🧭 Quick Summary
---

✅ Upload → 🧠 Extract → ✨ Summarize → 📄 Understand — All in seconds!
Your smart companion for document understanding and summarization.
