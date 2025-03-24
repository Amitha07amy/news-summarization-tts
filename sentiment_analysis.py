from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment

def compute_sentiment_distribution(articles):
    sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}

    for article in articles:
        sentiment = analyze_sentiment(article["content"]).lower()
        if sentiment in sentiment_counts:
            sentiment_counts[sentiment] += 1

    return sentiment_counts
