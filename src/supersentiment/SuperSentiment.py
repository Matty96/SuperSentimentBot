from binance.Binance import Binance
from coinbase.Coinbase import Coinbase
from sentiment.Sentiment import Sentiment
import matplotlib.pyplot as plt
import numpy as np

class SuperSentiment():
    """
    """
    def __init__(self):
        self.binance = Binance()
        self.coinbase = Coinbase()
        self.sentiment = Sentiment()
        self.buffer = []

        self.N = 5
        self.BTC = (1, 35, 30, 35, -27)
        self.ETH = (25, 32, 34, 20, -25)
        self.menStd = (2, 3, 4, 1, 2)
        self.womenStd = (3, 5, 2, 3, 3)
        self.ind = np.arange(self.N)    
        self.width = 0.35   


    def myPlot(self):
        fig, ax = plt.subplots()

        p2 = ax.bar(self.ind, self.ETH, self.width, yerr=self.menStd, label='ETH')
        p1 = ax.bar(self.ind, self.BTC, self.width, bottom=self.ETH, yerr=self.BTC, label='BTC')

        ax.axhline(0, color='grey', linewidth=0.8)
        ax.set_ylabel('Scores')
        ax.set_title('BTC/ETH price comparison')
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

    def check(self, exchage1:float, exchange2:float):
        if exchage1 - exchange2 >= 1:
            sentiment = self.checkSentiment()
            if sentiment == True:
                print("Stay")
            else:
                print("Sell")
        else:
            print("You should move money from wallets")

    def getPriceFromBinance(self, symbol):
        binancePrice = self.binance.crypto_to_tether(symbol)
        self.buffer.append(binancePrice)

    def getPriceFromCoinbase(self):
        coinbasePrice = self.coinbase.get_exchange()
        self.buffer.append(coinbasePrice)

    