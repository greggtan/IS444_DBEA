import requests, json
from functions import url
from dotenv import load_dotenv
import os

load_dotenv()

def getDepositAccountBalance():
    #Header
    serviceName = 'getDepositAccountBalance'
    userID = os.getenv('RETAIL_USER_ID')
    PIN = os.getenv('RETAIL_USER_PIN')
    OTP = os.getenv('RETAIL_OTP')
    #Content
    accountID = os.getenv('RETAIL_ACCOUNT_ID')
    
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
                        'accountID': accountID
                        }
                        }
    final_url="{0}?Header={1}&Content={2}".format(url(),json.dumps(headerObj),json.dumps(contentObj))
    response = requests.post(final_url)
    serviceRespHeader = response.json()['Content']['ServiceResponse']['ServiceRespHeader']
    errorCode = serviceRespHeader['GlobalErrorID']
    
    if errorCode == '010000':
        DepositAccount = response.json()['Content']['ServiceResponse']['DepositAccount']
        print("Balance: {}".format(DepositAccount['balance']))
    elif errorCode == '010041':
        print("OTP has expired.\nYou will receiving a SMS")
    else:
        print(serviceRespHeader['ErrorText'])

getDepositAccountBalance()
