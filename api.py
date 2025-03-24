from flask import Flask, request, jsonify, send_file
from news_extraction import fetch_news_articles
from summarization import summarize_text
from sentiment_analysis import analyze_sentiment
from comparative_analysis import compare_articles
from tts_hindi import text_to_speech
from utils import extract_topics
from googletrans import Translator  # For translation to Hindi
import os

app = Flask(__name__)

@app.route("/fetch_news", methods=["GET"])
def fetch_news():
    company = request.args.get("company", "Tesla")
    articles = fetch_news_articles(company, max_articles=7)  # Ensure max 7 articles

    combined_summary = ""
    for article in articles:
        article["summary"] = summarize_text(article["content"])
        article["sentiment"] = analyze_sentiment(article["summary"])
        article["topics"] = extract_topics(article["content"])  # Extract topics
        combined_summary += article["summary"] + " "  # Combine all summaries into one string

    # Translate combined summary to Hindi
    translator = Translator()
    combined_summary_hindi = translator.translate(combined_summary, src='en', dest='hi').text

    # Generate Hindi TTS for combined summaries
    audio_file_path = text_to_speech(combined_summary_hindi)  # Ensure this returns a file path

    # Compute comparative sentiment analysis
    sentiment_distribution, final_sentiment = compare_articles(articles)

    return jsonify({
        "company": company,
        "articles": articles,
        "sentiment_distribution": sentiment_distribution,
        "final_sentiment": final_sentiment,
        "audio_file": audio_file_path,  # Pass the file path here
        "combined_summary_hindi": combined_summary_hindi  # Showing the translated summary
    })

@app.route("/get_audio", methods=["GET"])
def get_audio():
    audio_path = "output.mp3"
    
    if os.path.exists(audio_path):
        return send_file(audio_path, mimetype="audio/mpeg")
    else:
        return jsonify({"error": "Audio file not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
