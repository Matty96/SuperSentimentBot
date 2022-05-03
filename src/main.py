# from cryptocom.CryptoCom import CryptoCom
from supersentiment.SuperSentiment import SuperSentiment

from binance.Binance import Binance

if __name__ == "__main__":
    superSentiment = SuperSentiment()

    binance = Binance()
    binancePrice = 0
    binancePrice = float(binance.get_crypto_price("BTCUSDT"))

    # TODO: like binance do with coinbase!
    coinbase = Binance()  # Coinbase()
    coinbase = 0
    coinbase = float(binance.get_crypto_price("BTCUSDT"))

    sentiment = superSentiment.check(binancePrice, coinbase)

    # print(result)

    # superSentiment.getPriceFromBinance('ETH')
    # superSentiment.getPriceFromBinance('BTC')

    #superSentiment.check(Binance, CryptoCom)

    # superSentiment.getPriceFromCoinbase()

    # print(f"Buffer: {superSentiment.buffer}")

    # superSentiment.myPlot()
