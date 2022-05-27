from binance.Binance import Binance
from coinbase.Coinbase import Coinbase
from supersentiment.SuperSentiment import SuperSentiment
from sentiment.Sentiment import Sentiment

if __name__ == "__main__":
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

    # superSentiment.check(exchange1, exchange2)
    # superSentiment.myPlot()
    print("")