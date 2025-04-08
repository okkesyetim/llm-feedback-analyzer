# 🧠 LLM Feedback Analyzer

A lightweight sentiment analysis API powered by **LangChain**, **Gemini (Google Generative AI)**, and **FastAPI**. It analyzes user feedback and returns both a sentiment classification and an actionable suggestion.

---

## 🚀 Features

- 🔍 **Sentiment Detection**: Positive, Negative, or Neutral
- 💡 **Recommendations**: Provides helpful suggestions based on sentiment
- 🤖 **LLM-Backed**: Uses Gemini via LangChain
- ⚡ **FastAPI** backend for quick and scalable integration

---

## 📦 Tech Stack

- [LangChain](https://www.langchain.com/)
- [Gemini API (Google Generative AI)](https://ai.google.dev/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [LangServe](https://python.langchain.com/docs/langserve/)

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/llm-feedback-analyzer.git
cd llm-feedback-analyzer
pip install -r requirements.txt

Create a `.env` file in the root directory:

# .env

GEMINI_API_KEY=your_gemini_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=SentimentSage

