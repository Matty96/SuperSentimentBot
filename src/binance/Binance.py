import requests
import pickledb
from datetime import datetime

class Binance:
    
    def __init__(self):
        self.pair_url = f'https://api.binance.com/api/v3/ticker/price'
        self.exchange_info_url = 'https://api.binance.com/api/v1/exchangeInfo'
        self.page = None

    def get_available_symbols(self):
        self.page = requests.get(self.exchange_info_url)
        response = [base['baseAsset'] for base in self.page.json()['symbols']]
        return response

    def get_crypto_price(self, pair):
         self.page = requests.get(f'{self.pair_url}?symbol={pair}')
         return self.page.json()['price']

    def crypto_to_tether(self, crypto_currency):
        #timeString = datetime.now()
        self.page = requests.get(f'{self.pair_url}?symbol={crypto_currency}USDT')
        # dbpickle = pickledb.load('PriceLogs.db', False)
        # #dbpickle.set('Binance Price', self.page.json()['price'])
        # dbpickle.load('Binance Price')
        # dbpickle.ladd('Binance Price' , self.page.json()['price'])
        
        # dbpickle.ladd('Binance Price', '20')
        # dbpickle.dump()
        print(f"{crypto_currency}: {self.page.json()['price']}" )
        file1 = open("PriceLog.txt", "a")
        file1.writelines('\n' + crypto_currency.upper() + " price on Binance: ")
        file1.writelines(self.page.json()['price'])

        #priceLog.writelines("\n" + symbol.upper() + " prices on Coinbase: ")

        return self.page.json()['price']