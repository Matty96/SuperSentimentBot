import tweepy
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
      self.numberOfTweets = 50
      self.negativeCount = 0
      self.neutralCount = 0
      self.positiveCount = 0
      self.sentiment = ''
      self.cryptoName = ''

    #This function is used to get the text sentiment
    def getSentiment(self, score):
      if score < 0:
        self.negativeCount = self.negativeCount + 1
        return 'Negative'
      if score == 0:
        self.neutralCount = self.neutralCount + 1
        return 'Neutral'
      if score > 0:
        self.positiveCount = self.positiveCount + 1
        return 'Positive'

    #This function is used to clean the tweets
    def cleanTwt(self, twt):
      twt = re.sub('#' + self.cryptoName, self.cryptoName, twt) #Removes the '#' from bitcoin
      # twt = re.sub('#bitcoin', 'bitcoin', twt) #Removes the '#' from bitcoin
      twt = re.sub('#[A-Za-z0-9]+', '', twt) #Removes any strings with a '#'
      twt = re.sub('\\n', '', twt) #Removing the '\n' string
      twt = re.sub('https?:\/\/\S+', '', twt) #Removes any hyperlinks
      return twt

    def check(self):
      CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
      CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
      ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
      ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")
      auth_handler = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
      auth_handler.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
      api = tweepy.API(auth_handler, wait_on_rate_limit=True)
      self.cryptoName = input("\nType the full name of the crypto on which you want to conduct the analysis: ")
      print("\nExecuting the sentiment analysis...")
      #Gather the tweets about bitcoin and filter out any retweets 'RT' (From 1st January 2022 till today's date)
      # search_term = '#bitcoin -filter:retweets'
      search_term = '#' + self.cryptoName + ' -filter:retweets'
      #Create a cursor object
      search_result = tweepy.Cursor(api.search_tweets, q=search_term, lang='en', tweet_mode= 'extended').items(self.numberOfTweets)
      # search_result = api.search_tweets(q=search_term, lang='en', since= '2021-01-01', tweet_mode= 'extended')

      # tweets = tweepy.Cursor(api.search, q=search_term, lang='en', since= '2022-01-01', tweet_mode= 'extended').items(2000)
      #Store the tweets in a variable and get the full text
      all_tweets = [tweet.full_text for tweet in search_result]

      #Create a dataframe to store the tweets with a column called 'Tweets'
      df = pd.DataFrame(all_tweets, columns = ['Tweets'])
      #Show the first 5 rows of data
      df.head(5)

      #Clean the tweets
      df['Cleaned_Tweets'] = df['Tweets'].apply(self.cleanTwt)
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
      
      #Create a column to store the text sentiment
      df['Sentiment'] = df['Polarity'].apply(self.getSentiment)
      #Show the data
      df.head()
      if self.negativeCount < self.positiveCount and self.positiveCount > self.neutralCount:
        self.sentiment = "Buy"
      elif self.negativeCount >= self.positiveCount and self.negativeCount > self.neutralCount:
        self.sentiment = "Sell"
      elif self.neutralCount > self.positiveCount and self.neutralCount > self.negativeCount:
        self.sentiment = "Stay"
      else:
        self.sentiment = "Stay"
      
      #Create a scatter plot to show the subjectivity and polarity
      plt.figure(figsize=(8,7))
      for i in range(0, df.shape[0]):
        plt.scatter(df['Polarity'][i], df['Subjectivity'][i], color='Purple')
      plt.title(self.cryptoName + ' sentiment analysis scatter plot')
      plt.xlabel('Polarity')
      plt.ylabel('Subjectivity (objective -> subjective)')
      plt.savefig(self.cryptoName + ' Scatter plot.png')
      plt.show()
      
      #Create a bar chart to show the count of Positive, Neutral and Negative sentiment
      df['Sentiment'].value_counts().plot(kind='bar')
      plt.title(self.cryptoName + ' sentiment analysis bar plot')
      plt.xlabel('Sentiment')
      plt.ylabel('Number of Tweets')
      plt.savefig(self.cryptoName + ' Bar plot.png')
      plt.show()
      print("\nTweets result")
      print(df['Sentiment'].value_counts())
      print(f"Number of tweets analysed: {self.numberOfTweets}")
      return self.sentiment

if __name__ == "__main__":
    s = Sentiment()
    result = s.check()
    print(f"result: {result}")



  