import os
import re
import tempfile
import streamlit as st
from datetime import datetime
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# ------------------- ENV SETUP -------------------
load_dotenv()

# Support both env variable names
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

# ------------------- PDF TOPIC EXTRACTION -------------------
def extract_topics_from_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    full_text = "\n".join([doc.page_content for doc in docs])
    lines = [line.strip() for line in full_text.splitlines() if line.strip()]

    topics = []
    current_topic = None
    current_text = []
    heading_pattern = re.compile(r'^[A-Z][A-Z\s\.\'\-:,0-9]+$')

    for line in lines:
        if heading_pattern.match(line) and len(line.split()) <= 8:
            if current_topic:
                topics.append({
                    "topic": current_topic.strip(),
                    "text": " ".join(current_text).strip()
                })
                current_text = []
            current_topic = line
        else:
            current_text.append(line)

    if current_topic and current_text:
        topics.append({
            "topic": current_topic.strip(),
            "text": " ".join(current_text).strip()
        })

    return topics, full_text


# ------------------- STREAMLIT UI CONFIG -------------------
st.set_page_config(page_title="Smart AI Document Content Extractor", page_icon="📘", layout="wide")

# Custom professional UI styling
st.markdown("""
    <style>
        body {
            background-color: #f5f6fa;
        }
        .block-container {
            max-width: 1000px;
            margin: auto;
            padding-top: 2rem;
        }
        h1 {
            text-align: center;
            color: #1a237e;
            font-family: 'Segoe UI', sans-serif;
            margin-bottom: 1rem;
        }
        .stButton button {
            background-color: #1a237e !important;
            color: white !important;
            border-radius: 8px !important;
            font-size: 16px !important;
            padding: 0.5rem 1.2rem !important;
        }
        .stButton button:hover {
            background-color: #303f9f !important;
        }
        .uploadedFile {
            text-align: center !important;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------- APP HEADER -------------------
st.title("📘 Smart AI Document Content Extractor")
st.markdown("""
Welcome to the **Smart AI Document Content Extractor**.  
Upload a PDF — the system will automatically extract key topics and generate a concise summary of the document using **Gemini 2.5 Flash**.
""")

# ------------------- FILE UPLOAD -------------------
uploaded_file = st.file_uploader("📂 Upload your PDF file below:", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    st.info("⏳ Processing your document... please wait.")

    try:
        results, full_text = extract_topics_from_pdf(temp_path)

        if not results:
            st.warning("⚠️ No recognizable topics found. Try a structured document with clear headings.")
        else:
            st.success(f"✅ Extracted {len(results)} topics successfully!")

            # Display topics neatly
            for i, item in enumerate(results, start=1):
                with st.expander(f"📖 {i}. {item['topic']}"):
                    st.write(item["text"] if item["text"] else "_(No content found under this heading)_")

            # ------------------- AI SUMMARY -------------------
            st.markdown("---")
            st.subheader("🧠 AI-Generated Summary")

            if st.button("✨ Generate Summary"):
                with st.spinner("🤖 Summarizing document with Gemini 2.5 Flash..."):
                    try:
                        llm = ChatGoogleGenerativeAI(
                            model="gemini-2.5-flash",
                            google_api_key=api_key  # ✅ Pass key explicitly
                        )

                        prompt = (
                            "Summarize the following document clearly and concisely. "
                            "Highlight key ideas, important names, and any factual details. "
                            "Make it structured, readable, and professional.\n\n"
                            f"{full_text[:15000]}"
                        )

                        response = llm.invoke(prompt)
                        st.success("✅ Summary generated successfully.")
                        st.markdown("### 📄 Summary")
                        st.markdown(response.content)

                    except Exception as e:
                        st.error(f"❌ Gemini API Error: {e}")

    except Exception as e:
        st.error(f"❌ Error processing the PDF: {e}")

else:
    st.info("👆 Please upload a PDF file to begin.")
