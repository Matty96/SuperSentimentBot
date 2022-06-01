import requests
import datetime
class Coinbase:
    def __init__(self):
        self.pair_url = f'https://api.coinbase.com/v2/prices/btc-usd/buy'
        self.exchange_info_url = ''
        self.page = None
        self.session = requests.session()
        self.headers = {'CB-VERSION':datetime.datetime.now().strftime("%Y-%m-%d")}
        # Cryptocurrencies available: BTC-ETH-ETC-ADA-XRP-SOL-DOT-AVAX-MATIC-UNI-BCH-MANA-MKR-BAT-LTC
    
    def get_price(self, symbol):
        #if self.headers['CB-VERSION'] != datetime.datetime.now().strftime("%Y-%m-%d"):
        response = self.session.get('https://api.coinbase.com/v2/prices/' + symbol + '-USD/buy', headers=self.headers)
        price = response.json()["data"]["amount"]

        #Print results
        print(f"{symbol}: {price}$")

        #Write on PriceLog.txt
        priceLog = open("PriceLog.txt", "a")
        priceLog.writelines("\n" + symbol.upper() + " price on Coinbase: ")
        priceLog.writelines(price)
        priceLog.close()
