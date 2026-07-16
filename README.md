# 📰 Aaj Ki Khabar — AI News Summarizer

A real-time news aggregator that fetches live headlines from NDTV and summarizes them using AI.

## Features
- Live news from NDTV RSS feeds
- AI-powered summarization using Groq LLaMA model
- Hindi and English language support
- Sentiment analysis (Positive / Negative / Neutral)
- Category filter: Top Stories, India, World, Sports, Technology

## Tech Stack
- Python
- Streamlit
- BeautifulSoup (web scraping)
- Groq API (LLaMA 3.3)

## Live Demo
[Click here to view live app](https://news-summarizer-hwofvkus4wfufehbb4nqmp.streamlit.app)

## Run Locally
```bash
pip install -r requirements.txt
export GROQ_API_KEY="your_key"
streamlit run app.py
```
