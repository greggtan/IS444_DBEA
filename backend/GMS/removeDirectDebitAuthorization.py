import requests, json
from functions import url
from dotenv import load_dotenv
import os

load_dotenv()

def removeDirectDebitAuthorization():
    #Header
    serviceName = 'removeDirectDebitAuthorization'
    userID = os.getenv('RETAIL_USER_ID')
    PIN = os.getenv('RETAIL_USER_PIN')
    OTP = os.getenv('RETAIL_OTP')
    #Content
    DirectDebitAuthorizationID = '0000000255'
    
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
                        'DirectDebitAuthorizationID': DirectDebitAuthorizationID
                        }
                        }
    final_url="{0}?Header={1}&Content={2}".format(url(),json.dumps(headerObj),json.dumps(contentObj))
    response = requests.post(final_url)
    print(response.json()['Content'])
    serviceRespHeader = response.json()['Content']['ServiceResponse']['ServiceRespHeader']
    errorCode = serviceRespHeader['GlobalErrorID']

    if errorCode == '010000':
        print('Organization has been removed')
    elif errorCode == '010041':
        print("OTP has expired.\nYou will receiving a SMS")
    else:
        print(serviceRespHeader['ErrorText'])

removeDirectDebitAuthorization()
