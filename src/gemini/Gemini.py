import requests
import datetime
class Gemini:
    def __init__(self):
        self.pair_url = f'https://api.gemini.com/v1'
        self.exchange_info_url = ''
        self.page = None
        # Cryptocurrencies available: BTC-ETH-SOL-DOGE-BCH-UNI-MANA-MKR-BAT-LTC

    def get_price(self, symbol):
        base_url = "https://api.gemini.com/v1"
        # response = requests.get(base_url + "/pricefeed")
        # symbols = pd.DataFrame(response.json())
        # symbols.tail()
        response = requests.get(base_url + "/pricefeed/" + symbol + "USD")
        jsonElement = response.json()
        price = jsonElement[0]["price"]
        
        #Print results
        print(f"{symbol}: {price}$")

        #Write on PriceLog.txt
        priceLog = open("PriceLog.txt", "a")
        priceLog.writelines("\n" + symbol.upper() + " price on Gemini: ")
        priceLog.writelines(price)
        priceLog.close()