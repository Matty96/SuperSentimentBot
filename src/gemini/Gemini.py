import json
import requests
import datetime
import pickledb
class Gemini:
    global btc_price, eth_price, file1
    def __init__(self):
        self.pair_url = f'https://api.gemini.com/v1'

    def get_value(self, symbol):
        #Get response
        base_url = "https://api.gemini.com/v1"
        # response = requests.get(base_url + "/pricefeed")
        # symbols = pd.DataFrame(response.json())
        # symbols.tail()
        response = requests.get(base_url + "/pricefeed/" + symbol + "USD")
        price = response.json()#['price']
        
        #Print results
        print(price)

        #Write on PriceLog.txt
        priceLog = open("PriceLog.txt", "a")
        priceLog.writelines("\n" + symbol.upper() + " price on Gemini: ")
        priceLog.writelines(btc_price)
        priceLog.close()

    

