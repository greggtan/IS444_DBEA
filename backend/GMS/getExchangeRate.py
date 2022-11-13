import requests, json
from functions import url
from getCurrencyList import getCurrencyList

def getExchangeRate():
    #Header
    serviceName = 'getExchangeRate'
    userID = ''
    PIN = ''
    OTP = ''
    baseCurrency = 'SGD'
    quoteCurrency = 'USD'
       
    
    headerObj = {
                        'Header': {
                        'serviceName': serviceName,
                        'userID': userID,
                        'PIN': PIN,
                        'OTP': OTP
                        }
                        }
    
    contentObj = {
                        'Content': {
                        'baseCurrency': baseCurrency,
                        'quoteCurrency': quoteCurrency
                        }
                        }
    
    final_url="{0}?Header={1}&Content={2}".format(url(),json.dumps(headerObj),json.dumps(contentObj))
    response = requests.post(final_url)
    serviceRespHeader = response.json()['Content']['ServiceResponse']['ServiceRespHeader']
    errorCode = serviceRespHeader['GlobalErrorID']

    if errorCode == '010000':
        base_currency_country_name = getCurrencyList(baseCurrency)[0]
        base_currency_currency_name = getCurrencyList(baseCurrency)[1]
        
        quote_currency_country_name = getCurrencyList(quoteCurrency)[0]
        quote_currency_currency_name = getCurrencyList(quoteCurrency)[1]

        print("Base Currency")
        print("Currency Code = {0}".format(baseCurrency))
        print("Country Name = {0}".format(base_currency_country_name))
        print("Currency Name = {0}".format(base_currency_currency_name))

        print()
        
        print("Quote Currency")
        print("Currency Code = {0}".format(quoteCurrency))
        print("Country Name = {0}".format(quote_currency_country_name))
        print("Currency Name = {0}".format(quote_currency_currency_name))

        print()
        
        FXSpotRateReadResponseObj = response.json()['Content']['ServiceResponse']['FX_SpotRate_Read-Response']
        print('Rate: {}'.format(FXSpotRateReadResponseObj['Rate']))
        
    elif errorCode == '010041':

       print("OTP has expired.\nYou will receiving a SMS")

    else:
       print(serviceRespHeader['ErrorText'])
            
getExchangeRate()
