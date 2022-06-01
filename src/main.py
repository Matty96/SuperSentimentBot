from supersentiment.SuperSentiment import SuperSentiment
from sentiment.Sentiment import Sentiment
import pandas as pd

if __name__ == "__main__":
    superSentiment = SuperSentiment()
    sentiment = Sentiment()
    exchange1 = 0.0
    exchange2 = 0.0
    cryptocurrencies = ['BTC', 'ETH', 'BCH', 'SOL', 'DOGE', 'LINK', 'UNI', 'MANA', 'BAT', 'LTC']

    print("\nBinance Exchange")
    for crypto in cryptocurrencies:
        superSentiment.getPriceFromBinance(crypto)
    print("\nCoinbase Exchange")
    for crypto in cryptocurrencies:
        superSentiment.getPriceFromCoinbase(crypto)
    print("\nGemini Exchange")
    for crypto in cryptocurrencies:
        superSentiment.getPriceFromGemini(crypto)
    print("")

    superSentiment.check(exchange1, exchange2)