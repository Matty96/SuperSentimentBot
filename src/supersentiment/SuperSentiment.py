import imp
from coinbase.Coinbase import Coinbase
from sentiment.Sentiment import Sentiment

import matplotlib.pyplot as plt
import numpy as np

class SuperSentiment():
    """
    """
    def __init__(self):
        self.coinbase = Coinbase()
        self.sentiment = Sentiment()
        self.buffer = []

        self.N = 5
        self.menMeans = (20, 35, 30, 35, -27)
        self.womenMeans = (25, 32, 34, 20, -25)
        self.menStd = (2, 3, 4, 1, 2)
        self.womenStd = (3, 5, 2, 3, 3)
        self.ind = np.arange(self.N)    
        self.width = 0.35   


    def myPlot(self):
        fig, ax = plt.subplots()

        p1 = ax.bar(self.ind, self.menMeans, self.width, yerr=self.menStd, label='Men')
        p2 = ax.bar(self.ind, self.womenMeans, self.width,
                    bottom=self.menMeans, yerr=self.womenStd, label='Women')

        ax.axhline(0, color='grey', linewidth=0.8)
        ax.set_ylabel('Scores')
        ax.set_title('Scores by group and gender')
        ax.set_xticks(self.ind, labels=['G1', 'G2', 'G3', 'G4', 'G5'])
        ax.legend()

        # Label with label_type 'center' instead of the default 'edge'
        ax.bar_label(p1, label_type='center')
        ax.bar_label(p2, label_type='center')
        ax.bar_label(p2)

        plt.show()

        
    def checkSentiment(self):
        # Look on tweets
        sentiment = self.sentiment.check()

        print("Machine Learning function -> Return sentiment")


        return sentiment


    def check(self, exchage1, exchange2):

        if exchage1 - exchange2 >= 1:
            sentiment = self.checkSentiment()
            if sentiment == True:
                print("Stay")
            else:
                print("Sell")
        else:
            print("move money from wallets")


    def getPrice(self, symbol):
         crypto = self.coinbase.crypto_to_tether(symbol)

         self.buffer.append(crypto)
