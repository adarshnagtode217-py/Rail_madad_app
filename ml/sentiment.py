from textblob import TextBlob


def analyze_sentiment(text):

    polarity = TextBlob(text).sentiment.polarity

    if polarity < -0.3:
        return "Negative"

    elif polarity > 0.3:
        return "Positive"

    else:
        return "Neutral"