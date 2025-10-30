📘 Smart AI Document Content Extractor

🚀 An intelligent document analysis tool powered by Google Gemini 2.5 Flash and LangChain.
Upload any PDF and instantly get summaries, insights, and AI-powered answers — all within an elegant Streamlit interface.

🧩 Overview

Smart AI Document Content Extractor is a lightweight, powerful application built using LangChain, Gemini 2.5 Flash, and FAISS vector search.

It allows you to:

📂 Upload PDF documents

🧠 Automatically extract and chunk the text

🗂️ Store embeddings in a FAISS vector database

✨ Generate AI-driven summaries

💬 Ask natural language questions about the content

All powered by Google’s Gemini 2.5 Flash model for lightning-fast and accurate responses.

🎯 Features
Feature	Description
📤 PDF Upload	Upload any PDF file through a simple drag-and-drop interface
🧠 Smart Summarization	Get a detailed summary of the uploaded document in seconds
💬 Question Answering	Ask context-aware questions about your PDF
⚡ Gemini 2.5 Flash	Utilizes Google’s latest multimodal LLM for speed and accuracy
🧮 FAISS Vector Search	Enables efficient semantic retrieval of document chunks
🎨 Modern Streamlit UI	Clean, responsive, and professional design
🔐 Secure API Handling	Uses environment variables to protect API keys
🏗️ Tech Stack
Component	Technology
Frontend	Streamlit
Backend AI	LangChain + Gemini 2.5 Flash
Vector Store	FAISS
Embeddings	HuggingFace Sentence Transformers
Environment Management	python-dotenv
PDF Parsing	PyPDF via LangChain loaders
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/smart-ai-document-extractor.git
cd smart-ai-document-extractor

2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate     # For Windows
source venv/bin/activate  # For macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Your Gemini API Key

Create a .env file in the project root:

GEMINI_API_KEY=your_gemini_flash_2_5_key_here


💡 Don’t expose your API key publicly — keep .env private!

5️⃣ Run the App
streamlit run app.py

🖥️ Usage Guide
▶️ Step 1: Launch the App

Once you run the app, Streamlit will open a local browser window (usually at http://localhost:8501).

📤 Step 2: Upload a PDF

Upload your document using the file uploader. The app will:

Extract text

Split it into chunks

Create vector embeddings

🧾 Step 3: Generate Summary

Click "✨ Generate Summary" to view an AI-generated summary of the document.

💬 Step 4: Ask Questions

Type your question in the input box (e.g., “What is the conclusion of this report?”) and hit Ask AI to get contextual answers.

📁 Project Structure
📁 Smart-AI-Document-Extractor/
│
├── app.py                 # Main Streamlit application
├── .env                   # Contains GEMINI_API_KEY
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

🧠 How It Works (Simplified Flow)

Load PDF → Using PyPDFLoader from LangChain

Split & Embed → Convert chunks to vector embeddings using HuggingFaceEmbeddings

Store in FAISS → For quick semantic retrieval

Query + RAG → Combine retrieved chunks + Gemini model for context-aware answers

Output → Display summarized or queried results in Streamlit UI

🖌️ UI Preview (Example)
📘 Smart AI Document Content Extractor
────────────────────────────────────
📂 Upload PDF: [Choose File]
✅ PDF loaded successfully with 25 chunks

✨ Generate Summary
🧾 Document Summary:
• The document discusses renewable energy...
• Key points include cost efficiency and storage...

💬 Ask Questions:
[ What are the challenges of solar adoption? ]
→ The main challenges include cost, policy, and awareness.

🚀 Future Improvements

📊 Extract structured data tables from PDFs

🗣️ Support for multimodal input (image + text)

🌐 Cloud deployment on Streamlit Cloud or Hugging Face Spaces

🧩 Chat history memory and follow-up context
