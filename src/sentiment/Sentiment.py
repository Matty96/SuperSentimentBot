import tweepy
import sys
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import os
from textblob import TextBlob
from dotenv import load_dotenv #Get environment variable from .env file
load_dotenv()
plt.style.use('fivethirtyeight')

class Sentiment():
    """
    Sentiment on crypto based on tweets
    """
    def __init__(self):
        print("Sentiment Analyzer")

    def check(self):
      CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
      CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
      ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
      ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")
      auth_handler = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
      auth_handler.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
      api = tweepy.API(auth_handler, wait_on_rate_limit=True)
      #search_term = 'stocks'
      #Gather the tweets about Bitcoin and filter out any retweets 'RT' (From 1st January 2022 till today's date)
      search_term = '#bitcoin -filter:retweets'
      #Create a cursor object

      search_result = api.search_tweets(q=search_term, lang='en', since= '2022-01-01', tweet_mode= 'extended')

      # tweets = tweepy.Cursor(api.search, q=search_term, lang='en', since= '2022-01-01', tweet_mode= 'extended').items(2000)
      #Store the tweets in a variable and get the full text
      all_tweets = [tweet.full_text for tweet in search_result]

      #Create a dataframe to store the tweets with a column called 'Tweets'
      df = pd.DataFrame(all_tweets, columns = ['Tweets'])
      #Show the first 5 rows of data
      df.head(5)

      #Create a function to clean the tweets
      def cleanTwt(twt):
        twt = re.sub('#bitcoin', 'bitcoin', twt) #Removes the '#' from Bitcoin
        twt = re.sub('#[A-Za-z0-9]+', '', twt) #Removes any strings with a '#'
        twt = re.sub('\\n', '', twt) #Removing the '\n' string
        twt = re.sub('https?:\/\/\S+', '', twt) #Removes any hyperlinks
        return twt

      #Clean the tweets
      df['Cleaned_Tweets'] = df['Tweets'].apply(cleanTwt)
      #Show the data set
      df.head(10)

      #Create a function to get the subjectivity
      def getSubjectivity(twt):
        return TextBlob(twt).sentiment.subjectivity
      #Create a function to get the polarity
      def getPolarity(twt):
        return TextBlob(twt).sentiment.polarity
      #Create 2 columns 'Subjectivity' and 'Polarity'
      df['Subjectivity'] = df['Cleaned_Tweets'].apply(getSubjectivity)
      df['Polarity'] = df['Cleaned_Tweets'].apply(getPolarity)
      #Show the data
      df.head()

      #Create a function to get the text sentiment
      def getSentiment(score):
        if score < 0:
          return 'Negative'
        elif score == 0:
          return 'Neutral'
        else:
          return 'Positive'

      #Create a column to store the text sentiment
      df['Sentiment'] = df['Polarity'].apply(getSentiment)
      #Show the data
      df.head()

      #Create a scatter plot to show the subjectivity and polarity
      plt.figure(figsize=(8,6))
      for i in range(0, df.shape[0]):
        plt.scatter(df['Polarity'][i], df['Subjectivity'][i], color='Purple')
      plt.title('Sentiment analysis scatter plot')
      plt.xlabel('Polarity')
      plt.ylabel('Subjectivity (objective -> subjective)')
      plt.show()
      #return True

if __name__ == "__main__":
    s = Sentiment()
    result = s.check()
    print(f"result: {result}")



  