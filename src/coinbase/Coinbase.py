import json
import requests
import datetime
import pickledb
class Coinbase:
    global btc_price, eth_price, file1
    def __init__(self):
        self.pair_url = f'https://api.coinbase.com/v2/prices/btc-usd/buy'
        self.exchange_info_url = ''

        self.page = None
        self.session = requests.session()
        self.headers = {'CB-VERSION':datetime.datetime.now().strftime("%Y-%m-%d")}
    
    #COINBASE
    def get_exchange(self, symbol):
        #coinbaseFirstSymbol = "btc" #input("Enter a crypto symbol for Coinbase: ")

        #Get response
        #if self.headers['CB-VERSION'] != datetime.datetime.now().strftime("%Y-%m-%d"):
        btc_r = self.session.get('https://api.coinbase.com/v2/prices/' + symbol + '-USD/buy', headers=self.headers)
        btc_price = btc_r.json()["data"]["amount"]

        #Print results
        print(f"{symbol}: {btc_price}")

        #Write on PriceLog.txt
        priceLog = open("PriceLog.txt", "a")
        priceLog.writelines("\n" + symbol.upper() + " price on Coinbase: ")
        priceLog.writelines(btc_price)
        priceLog.close()

    #GEMINI
    # print("\nGemini API")
    # symbolForGemini = "btc" #input("Enter a crypto symbol for Gemini: ")
    # #print(f'You entered {symbolForGemini.upper()}')

    # #Get response
    # response = requests.get("https://min-api.cryptocompare.com/data/price?fsym=" + symbolForGemini.upper() + "&tsyms=EUR,GBP,USD,JPN,CNY")
    # print(symbolForGemini.upper() + ' ' + str(response.json()))

    # #Write on PriceLog.txt
    # priceLog = open("PriceLog.txt", "a")
    # priceLog.writelines("\n" + symbolForGemini.upper() + " prices on Gemini: \n")
    # priceLog.writelines(symbolForGemini.upper() + ': ' + str(response.json()) + '\n')
    # priceLog.close()


