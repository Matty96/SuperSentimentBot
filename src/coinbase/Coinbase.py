import json
import requests
import datetime
import pickledb
class Coinbase:
    global btc_price, eth_price, ltc_price, file1
    def __init__(self):
        self.pair_url = f'https://api.coinbase.com/v2/prices/btc-usd/buy'
        self.exchange_info_url = ''

        self.page = None
        self.session = requests.session()
        self.headers = {'CB-VERSION':datetime.datetime.now().strftime("%Y-%m-%d")}
    
    #COINBASE
    def get_exchange(self):
        print("Coinbase")
        coinbaseFirstSymbol = "btc" #input("Enter a crypto symbol for Coinbase: ")
        #print(f'You entered {symbolForCoinbase.upper()}')
        coinbaseSecondSymbol = "eth"

        #Get response
        #if self.headers['CB-VERSION'] != datetime.datetime.now().strftime("%Y-%m-%d"):
        btc_r = self.session.get('https://api.coinbase.com/v2/prices/' + coinbaseFirstSymbol + '-USD/buy', headers=self.headers)
        btc_price = btc_r.json()["data"]["amount"]
        btc_r = self.session.get('https://api.coinbase.com/v2/prices/' + coinbaseSecondSymbol + '-USD/buy', headers=self.headers)
        eth_price = btc_r.json()["data"]["amount"]

        #Print results
        print("BTC: " + btc_price)
        print("ETH: " + eth_price + "\n")

        #Write on PriceLog.txt
        priceLog = open("PriceLog.txt", "a")
        priceLog.writelines("\n" + coinbaseFirstSymbol.upper() + " prices on Coinbase: ")
        priceLog.writelines(btc_price)
        priceLog.close()



    # #COINDESK
    # def jprint(obj):
    #     text = json.dumps(obj, sort_keys=True, indent=4)
    #     print(text)

    # print("\nCoindesk API")
    # pricesBTC=['Bitcoin: ']

    # #Get response
    # response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # price_data=response.json()['bpi']
    # for c in price_data:
    #     amount = price_data[c]['rate']
    #     curr_code = price_data[c]['code']
    #     price = str(curr_code) + ": " + str(amount) + ", " 
    #     pricesBTC.insert(1, price)
    
    # #Print results
    # print(pricesBTC)

    # #Write on PriceLog.txt

    # dbpickle = pickledb.load('PriceLogs.db', False)
    # #dbpickle.set('Binance Price', self.page.json()['price'])
    # dbpickle.lcreate('Coindesk Price')
    # dbpickle.ladd('Coindesk Price' , '0')
    
    # #dbpickle.ladd('Coindesk Price', '20')
    # dbpickle.dump()

    # priceLog = open("PriceLog.txt", "a")
    # priceLog.writelines("BTC prices on Coindesk: \n")
    # priceLog.writelines(pricesBTC)
    # priceLog.close()
    


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


