import requests, json
from functions import url,getRecord
from getBillingOrganizations import getBillingOrganizations
from dotenv import load_dotenv
import os

load_dotenv()

def getDirectDebitAuthorizationList():
    #Header
    serviceName = 'getDirectDebitAuthorizationList'
    userID = os.getenv('RETAIL_USER_ID')
    PIN = os.getenv('RETAIL_USER_PIN')
    OTP = os.getenv('RETAIL_OTP')
    headerObj = {
                        'Header': {
                        'serviceName': serviceName,
                        'userID': userID,
                        'PIN': PIN,
                        'OTP': OTP
                        }
                        }
    final_url="{0}?Header={1}".format(url(),json.dumps(headerObj))
    response = requests.post(final_url)

    serviceRespHeader = response.json()['Content']['ServiceResponse']['ServiceRespHeader']
    errorCode = serviceRespHeader['GlobalErrorID']

    if errorCode == '010000':
        dda_list = response.json()['Content']['ServiceResponse']['AuthorizationList']
        if dda_list == {}:
            print("No record found!")
        else:
            dda_list = dda_list['Authorization']
            recordCount = getRecord(dda_list)
            if recordCount>1:                 
                for i in range(0,recordCount,1):
                        directDebitAuthorizationList = dda_list[i]
                        print("\nBilling Organisation code Bank Code : {}".format(directDebitAuthorizationList['BillingOrgBankCode']))
                        print("Customer Bank Code : {}".format(directDebitAuthorizationList['CustomerBankCode']))
                        print("Customer Account ID : {}".format(directDebitAuthorizationList['CustomerAccountID']))
                        print("Billing Organisation ID : {}".format(directDebitAuthorizationList['BillingOrgID']))
                        print("CustomerID : {}".format(directDebitAuthorizationList['CustomerID']))
                        print("Billing Organisation Account ID : {}".format(directDebitAuthorizationList['BillingOrgAccountID']))
                        print("Billing Organisation: {}".format(getBillingOrganizations(directDebitAuthorizationList['BillingOrgAccountID'])))
                        print("Creation Date : {}".format(directDebitAuthorizationList['CreationDate']))
                        print("Direct Debit Authorization ID : {}".format(directDebitAuthorizationList['DirectDebitAuthorizationID']))
            elif recordCount == 0:
                # print("\nBilling Organisation code Bank Code : {}".format(dda_list['BillingOrgBankCode']))
                print("Customer Bank Code : {}".format(dda_list['CustomerBankCode']))
                print("Customer Account ID : {}".format(dda_list['CustomerAccountID']))
                print("Billing Organisation ID : {}".format(dda_list['BillingOrgID']))
                print("CustomerID : {}".format(dda_list['CustomerID']))
                print("Billing Organisation Account ID : {}".format(dda_list['BillingOrgAccountID']))
                print("Billing Organisation: {}".format(getBillingOrganizations(dda_list['BillingOrgAccountID'])))
                print("Creation Date : {}".format(dda_list['CreationDate']))
    elif errorCode == '010041':
        print("OTP has expired.\nYou will receiving a SMS")
    else:
        print(serviceRespHeader['ErrorText'])
                            
getDirectDebitAuthorizationList()
