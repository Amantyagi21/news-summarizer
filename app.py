import streamlit as st
from scraper import news_lao
from summarizer import summarize_karo, sentiment_karo

st.title("📰 Aaj Ki Khabar")
st.subheader("AI se summarized — 30 seconds mein poori news")

col1, col2 = st.columns(2)

with col1:
    category = st.selectbox(
        "Category chuno:",
        ["Top Stories", "India", "World", "Sports", "Technology"]
    )

with col2:
    language = st.selectbox(
        "Language chuno:",
        ["Hindi", "English"]
    )

category_urls = {
    "Top Stories": "https://feeds.feedburner.com/ndtvnews-top-stories",
    "India": "https://feeds.feedburner.com/ndtvnews-india-news",
    "World": "https://feeds.feedburner.com/ndtvnews-world-news",
    "Sports": "https://feeds.feedburner.com/ndtvnews-sports",
    "Technology": "https://feeds.feedburner.com/ndtvnews-tech-gadgets"
}

if st.button("News Lao"):
    with st.spinner("News aa rahi hai..."):
        articles = news_lao(category_urls[category])
    
    for article in articles:
        sentiment = sentiment_karo(article['title'])
        if sentiment == "Positive":
            st.success(f"🟢 Positive  |  {article['title']}")
        elif sentiment == "Negative":
            st.error(f"🔴 Negative  |  {article['title']}")
        else:
            st.warning(f"🟡 Neutral  |  {article['title']}")
        
        with st.spinner("Summary ban rahi hai..."):
            summary = summarize_karo(article['description'], language)
        st.write(summary)
        st.divider() 