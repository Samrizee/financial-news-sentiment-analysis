import nltk  # type: ignore
from nltk.sentiment import SentimentIntensityAnalyzer  # type: ignore

def Initialize_Sentiment_Analyzer():
    nltk.download('vader_lexicon')
    return SentimentIntensityAnalyzer()

def sentiment_vader(text, sia):
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores['compound']

def Sentiment_Analyzer(data):
    sia = Initialize_Sentiment_Analyzer()
    data['sentiment'] = data['headline'].apply(lambda text: sentiment_vader(text, sia))
    print(data['sentiment'].describe())
    return data
