from binance.Binance import Binance
from coinbase.Coinbase import Coinbase
from supersentiment.SuperSentiment import SuperSentiment
from sentiment.Sentiment import Sentiment
import json, requests
import pandas as pd

from .datastore.Datastore import Datastore

if __name__ == "__main__":

    datastore = Datastore()
    superSentiment = SuperSentiment()
    sentiment = Sentiment()
    print("Binance")
    exchange1 = superSentiment.getPriceFromBinance('BTC')
    superSentiment.getPriceFromBinance('ETH')
    print("\nCoinbase")
    exchange2 = superSentiment.getPriceFromCoinbase('BTC')
    superSentiment.getPriceFromCoinbase('ETH')
    #superSentiment.checkSentiment()
    #print(f"Binance \nBTC and ETH: {superSentiment.buffer} \n")
    print("\nGemini")
    base_url = "https://api.gemini.com/v1"
    # response = requests.get(base_url + "/pricefeed")
    # symbols = pd.DataFrame(response.json())
    # symbols.tail()
    response = requests.get(base_url + "/pricefeed/BTCUSD")
    price = response.json()#['price']
    print(price)
    
    # superSentiment.check(exchange1, exchange2)
    # superSentiment.myPlot()
    print("")
