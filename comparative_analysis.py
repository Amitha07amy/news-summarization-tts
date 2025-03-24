def compare_articles(articles):
    sentiment_count = {"Positive": 0, "Negative": 0, "Neutral": 0}
    
    for article in articles:
        sentiment_count[article["sentiment"]] += 1

    final_sentiment = "Mostly positive coverage" if sentiment_count["Positive"] > sentiment_count["Negative"] else "Mixed or negative sentiment"

    return sentiment_count, final_sentiment
