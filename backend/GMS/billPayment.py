import requests, json
from functions import url
from dotenv import load_dotenv
import os

load_dotenv()

def billPayment():
    #Header
    serviceName = 'billPayment'
    userID = os.getenv('RETAIL_USER_ID')
    PIN = os.getenv('RETAIL_USER_PIN')
    OTP = os.getenv('RETAIL_OTP')
    #Content
    accountFrom = os.getenv('RETAIL_ACCOUNT_ID')
    accountTo = os.getenv('STARHUB_ACCOUNT_ID')
    transactionAmount = '100'
    transactionReferenceNumber = '12332'
    narrative = '2'
    
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
                        'transactionAmount': transactionAmount,
                        'transactionReferenceNumber': transactionReferenceNumber ,
                        'narrative': narrative
                        }
                        }
    final_url="{0}?Header={1}&Content={2}".format(url(),json.dumps(headerObj),json.dumps(contentObj))
    response = requests.post(final_url)
    serviceRespHeader = response.json()['Content']['ServiceResponse']['ServiceRespHeader']
    errorCode = serviceRespHeader['GlobalErrorID']
    
    if errorCode == '010000':
        ServerResponse = response.json()['Content']['ServiceResponse']
        print("Balance After Transferring: ${:.2f} ".format(float(ServerResponse['BalanceAfter']['_content_'])))
        print("Transaction ID: ", ServerResponse['TransactionID']['_content_'])
        print("Balance Before Transferring: ${:.2f}".format( float(ServerResponse['BalanceBefore']['_content_'])))
    elif errorCode == '010041':
        print("OTP has expired.\nYou will receiving a SMS")  
    else:
        print(serviceRespHeader['ErrorText'])
billPayment()
