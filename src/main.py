from binance.Binance import Binance
from supersentiment.SuperSentiment import SuperSentiment
from sentiment.Sentiment import Sentiment

if __name__ == "__main__":
    superSentiment = SuperSentiment()
    sentiment = Sentiment()
    print("Binance")
    superSentiment.getPriceFromBinance('BTC')
    superSentiment.getPriceFromBinance('ETH')
    print("")

    #superSentiment.check(Binance, CryptoCom)

    superSentiment.getPriceFromCoinbase()
    superSentiment.checkSentiment()
    #print(f"Binance \nBTC and ETH: {superSentiment.buffer} \n")

    superSentiment.myPlot()