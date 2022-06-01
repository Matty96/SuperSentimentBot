from binance.Binance import Binance
from coinbase.Coinbase import Coinbase
from gemini.Gemini import Gemini
from sentiment.Sentiment import Sentiment
import matplotlib.pyplot as plt
import numpy as np

class SuperSentiment():
    """
    Algorithm to determine the best action to take
    """
    def __init__(self):
        self.binance = Binance()
        self.coinbase = Coinbase()
        self.gemini = Gemini()
        self.sentiment = Sentiment()
        self.buffer = [0]
        self.symbol = ""

    def checkSentiment(self):
        # Look on tweets
        sentiment = self.sentiment.check()
        print(f"\nThe sentiment returned from the machine learning function is: {sentiment}\n")
        return sentiment

    def check(self, exchange1: float, exchange2: float):
        buyFrom = "Exchange1"
        sellFrom = "Exchange2"
        self.symbol = input("Choose the crypto on which you want to conduct the analysis: ")
        exchangeName1 = input("Enter the name of the first exchange to use: ")
        exchangeName2 = input("Enter the name of the second exchange to use: ")

        priceLog = open("PriceLog.txt", "r")
        Lines = priceLog.readlines()
        if(exchangeName1 == "Binance"):
            for line in Lines:
                if line.startswith(f'{self.symbol} price on Binance: '):
                    priceFromBinance = line[22:]
                    exchange1 = float(priceFromBinance)
        elif(exchangeName1 == "Coinbase"):
            for line in Lines:
                if line.startswith(f'{self.symbol} price on Coinbase: '):
                    priceFromCoinbase = line[23:]
                    exchange1 = float(priceFromCoinbase)
        elif(exchangeName1 == "Gemini"):
            for line in Lines:
                if line.startswith(f'{self.symbol} price on Gemini: '):
                    priceFromGemini = line[21:]
                    exchange1 = float(priceFromGemini)
        
        if(exchangeName2 == "Binance"):
            for line in Lines:
                if line.startswith(f'{self.symbol} price on Binance: '):
                    priceFromBinance = line[22:]
                    exchange2 = float(priceFromBinance)
        elif(exchangeName2 == "Coinbase"):
            for line in Lines:
                if line.startswith(f'{self.symbol} price on Coinbase: '):
                    priceFromCoinbase = line[23:]
                    exchange2 = float(priceFromCoinbase)
        elif(exchangeName2 == "Gemini"):
            for line in Lines:
                if line.startswith(f'{self.symbol} price on Gemini: '):
                    priceFromGemini = line[21:]
                    exchange2 = float(priceFromGemini)
        
            # if line.startswith(f'{self.symbol} price on Gemini: '):
            #     priceFromGemini = line[21:]
            #     exchange3 = float(priceFromGemini)
        priceLog.close()
        print("\nLast prices retrieved from PriceLog.txt")
        print(f"{self.symbol} price on {exchangeName1}, set as Exchange1: {exchange1}$")
        print(f"{self.symbol} price on {exchangeName2}, set as Exchange2: {exchange2}$")

        if (exchange1 - exchange2 >= 0):
            buyFrom = "Exchange2"
            sellFrom = "Exchange1"
            # print(f"Buy on: {buyFrom}")
            # print(f"Sell on: {sellFrom}\n")
        elif (exchange2 - exchange1 >= 0):
            buyFrom = "Exchange1"
            sellFrom = "Exchange2"
            # print(f"Buy on: {buyFrom}")
            # print(f"Sell on: {sellFrom}\n")

        sentiment = self.checkSentiment()

        if sentiment == "Stay":
            print(f"The suggested action to be taken is to Stay\n")
        elif sentiment == "Buy":
            print(f"The suggested action to be taken is to Buy on {buyFrom} and Sell on {sellFrom}\n")
        elif sentiment == "Sell":
            print(f"The suggested action to be taken is to Sell on {sellFrom} and Buy on {buyFrom}\n")
        
    def getPriceFromBinance(self, symbol):
        binancePrice = self.binance.get_price(symbol)
        self.buffer.append(binancePrice)

    def getPriceFromCoinbase(self, symbol):
        coinbasePrice = self.coinbase.get_price(symbol)
        self.buffer.append(coinbasePrice)

    def getPriceFromGemini(self, symbol):
        geminiPrice = self.gemini.get_price(symbol)
        self.buffer.append(geminiPrice)

    

