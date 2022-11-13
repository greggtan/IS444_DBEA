from flask import Blueprint, jsonify, request
import requests, json
from apis.functions import url,getRecord

stocks_api = Blueprint('stocks_api', __name__)

@stocks_api.route('/getStocks', methods=['GET'])

# Get stocks symbol
def getStockSymbols():
    serviceName = 'getStockSymbols'
    headerObj = {
                        'Header': {
                        'serviceName': serviceName,
                        'userID': 'HANDCHIA',
                        'PIN': '123456',
                        'OTP': '999999'
                        }
                        }
    final_url="{0}?Header={1}".format(url(),json.dumps(headerObj))
    response = requests.post(final_url)

    stockSymbols = response.json()['Content']['ServiceResponse']['StockSymbolList']['StockSymbol']
    Symbol_List= []
    Company_List = []
    NYSEList = ['A', 'AA', 'AAP', 'ABC', 'AMN', 'IBM', 'T', 'UBER', "DIS", "HRB"]
    NASDAQList = ['AZN', 'DWAC', 'META', 'AMZN', 'AAPL', 'GOOG', 'MSFT', 'NFLX', 'TSLA', 'TIGR', 'VOD']

    for i in range(len(stockSymbols)):
        symbol = stockSymbols[i]
        companyName = symbol['company']
        symbol = symbol['symbol']
        updatedSymbol = ''
        
        if "-" in symbol or "." in symbol or "^" in symbol or symbol == "FB" or symbol == "MSBHY" or symbol == "STI" or symbol == "CAD":
            updatedSymbol = ''
            pass
        
        elif symbol in NYSEList:
            updatedSymbol = 'NYSE:' + symbol

        elif symbol in NASDAQList:
            updatedSymbol = 'NASDAQ:' + symbol

        elif symbol == "YAHOY":
            updatedSymbol = 'OTC:' + symbol

        else:
            updatedSymbol = symbol

        if updatedSymbol != '':
            Symbol_List.append(updatedSymbol)
        
    return(Symbol_List)
