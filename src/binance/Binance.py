import requests
import datetime
class Binance:
    def __init__(self):
        self.pair_url = f'https://api.binance.com/api/v3/ticker/price'
        self.exchange_info_url = f'https://api.binance.com/api/v1/exchangeInfo'
        self.page = None
        # Cryptocurrencies available: BTC-ETH-ETC-ADA-XRP-SOL-DOT-AVAX-MATIC-UNI-BCH-MANA-MKR-BAT-LTC

    # def get_available_symbols(self):
    #     self.page = requests.get(self.exchange_info_url)
    #     response = [base['baseAsset'] for base in self.page.json()['symbols']]
    #     return response

    # def get_crypto_price(self, pair):
    #      self.page = requests.get(f'{self.pair_url}?symbol={pair}')
    #      return self.page.json()['price']

    def get_price(self, crypto_currency):
        #timeString = datetime.now()
        self.page = requests.get(f'{self.pair_url}?symbol={crypto_currency}USDT')

        #Print results
        print(f"{crypto_currency}: {self.page.json()['price']}$" )

        #Write on PriceLog.txt
        priceLog = open("PriceLog.txt", "a")
        priceLog.writelines('\n' + crypto_currency.upper() + " price on Binance: ")
        priceLog.writelines(self.page.json()['price'])
        priceLog.close()
        return self.page.json()['price']