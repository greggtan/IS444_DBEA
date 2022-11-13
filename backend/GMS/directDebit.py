import requests, json
from functions import url
from dotenv import load_dotenv
import os

load_dotenv()
    
def directDebit():
    #Header
    serviceName = 'directDebit'
    userID = os.getenv('STARHUB_USER_ID')
    PIN = os.getenv('STARHUB_USER_PIN')
    OTP = os.getenv('BILLORG_OTP')

    #Content
    accountFrom = os.getenv('STARHUB_ACCOUNT_ID')
    accountTo = os.getenv('RETAIL_ACCOUNT_ID')
    transactionAmount = '100'
    transactionReferenceNumber = '1'
    narrative = 'bill'

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
                        'accountFrom': accountFrom,
                        'accountTo': accountTo,
                        'transactionAmount':transactionAmount,
                        'transactionReferenceNumber':transactionReferenceNumber,
                        'narrative':narrative
                        }
                        }
    final_url="{0}?Header={1}&Content={2}".format(url(),json.dumps(headerObj),json.dumps(contentObj))
    response = requests.post(final_url)
    serviceRespHeader = response.json()['Content']['ServiceResponse']['ServiceRespHeader']
    errorCode = serviceRespHeader['GlobalErrorID']

    if errorCode == '010000':
        
        ServerResponse = response.json()['Content']['ServiceResponse']
        print("Balance After Transferring ${}: ${:.2f}".format(transactionAmount, float(ServerResponse['BalanceAfter']['_content_'])))
        print("Transaction ID: ", ServerResponse['TransactionID']['_content_'])
        print("Balance Before Tranferring ${}: ${:.2f}".format(transactionAmount, float(ServerResponse['BalanceBefore']['_content_'])))
    elif errorCode == '010041':
        print("OTP has expired.\nYou will receiving a SMS")
    else:
        print(serviceRespHeader)
        print(serviceRespHeader['ErrorText'])

directDebit()
