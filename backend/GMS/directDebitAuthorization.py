import requests, json
from functions import url
from dotenv import load_dotenv
import os

load_dotenv()
    
def directDebitAuthorization():
    #Header
    serviceName = 'directDebitAuthorization'
    userID = os.getenv('RETAIL_USER_ID')
    PIN = os.getenv('RETAIL_USER_PIN')
    OTP = os.getenv('RETAIL_OTP')
    #Content
    customerAccountID = os.getenv('RETAIL_ACCOUNT_ID')
    billingOrgAccountID = os.getenv('STARHUB_ACCOUNT_ID')
    
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
                        'customerAccountID': customerAccountID,
                        'billingOrgAccountID': billingOrgAccountID
                        }
                        }
    final_url="{0}?Header={1}&Content={2}".format(url(), json.dumps(headerObj), json.dumps(contentObj))
    response = requests.post(final_url)
    serviceRespHeader = response.json()['Content']['ServiceResponse']['ServiceRespHeader']
    errorCode = serviceRespHeader['GlobalErrorID']
    if errorCode == '010000':
        ServerResponse = response.json()['Content']['ServiceResponse']
        print("Direct Debit Authorization ID: {}".format(ServerResponse['DirectDebitAuthorizationID']['_content_']))
    elif errorCode == '010041':
        print("OTP has expired.\nYou will receiving a SMS")
    else:
        print('error')
        print(serviceRespHeader['ErrorText'])

directDebitAuthorization()
