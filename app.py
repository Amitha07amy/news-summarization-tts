import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/fetch_news"

st.title("News Summarization and Text to Speech Application")

company = st.text_input("Enter a Topic", " ")

if st.button("Fetch News"):
    response = requests.get(f"{API_URL}?company={company}")

    if response.status_code == 200:
        data = response.json()

        st.subheader(f"Headlines Of:: {data['company']}")
        st.subheader("Articles:")

        for i, article in enumerate(data["articles"], 1):
            st.markdown(f"### {i}. **{article['title']}**")
            st.markdown(f"**Summary:** {article['summary']}")
            st.markdown(f"**Sentiment:** {article['sentiment']}")
            st.markdown(f"**Topics:** {', '.join(article['topics']) if article['topics'] else 'N/A'}")
            st.markdown(f"[Read More]({article['url']})")

        st.subheader("Sentiment Distribution:")
        sentiment_dist = data.get("sentiment_distribution", {})
        for sentiment, count in sentiment_dist.items():
            st.write(f"{sentiment.capitalize()}: {count}")

        st.subheader("Coverage Differences:")
        for idx, comparison in enumerate(data.get("coverage_comparisons", []), 1):
            st.markdown(f"**Comparison {idx}:** {comparison['comparison']}")
            st.markdown(f"**Impact:** {comparison['impact']}")

        st.subheader("Final Sentiment Analysis:")
        st.write(data["final_sentiment"])

        st.subheader("Combined Hindi Summary:")
        st.write(data.get("combined_summary_hindi", "No Summary Available"))

        # Display audio player with the correct path
        st.subheader("Audio:")
        st.audio(data['audio_file'])  # Use the audio file path returned from the API

    else:
        st.error("Error fetching data. Check API logs for details.")
