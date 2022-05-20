from binance.Binance import Binance
from supersentiment.SuperSentiment import SuperSentiment
from sentiment.Sentiment import Sentiment

if __name__ == "__main__":
    superSentiment = SuperSentiment()
    sentiment = Sentiment()
    
    #superSentiment.getPriceFromBinance('ETH')
    superSentiment.getPriceFromBinance('BTC')

    #superSentiment.check(Binance, CryptoCom)

    superSentiment.getPriceFromCoinbase()

    "spot/ticker:BTC_USDT"

    print(f"Buffer: {superSentiment.buffer}")

    superSentiment.myPlot()