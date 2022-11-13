import requests, json
from functions import url
from dotenv import load_dotenv
import os

load_dotenv()

def getDepositAccountDetails():
    #Header
    serviceName = 'getDepositAccountDetails'
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
        depositAccount = response.json()['Content']['ServiceResponse']['DepositAccount']
        print("Is Service Charge Waived: {}".format(depositAccount['isServiceChargeWaived']))
        print("Minor Status: {}".format(depositAccount['casaaccount']['minorStatus']))
        print("Due Interest Amount: {}".format(depositAccount['casaaccount']['dueInterestAmount']))
        print("Is Restricted: {}".format(depositAccount['casaaccount']['isRestricted']))
        print("Deposit Term: {}".format(depositAccount['casaaccount']['depositTerm']))
        print("Interest Payout Account: {}".format(depositAccount['casaaccount']['interestPayoutAccount']))
        print("Parent Account Flag: {}".format(depositAccount['casaaccount']['parentAccountFlag']))
        print("Account Close Date: {}".format(depositAccount['casaaccount']['accountCloseDate']))
        print("Minimum Amount: {}".format(depositAccount['casaaccount']['minimumAmount']))
        print("Accrue Interest Amount: {}".format(depositAccount['casaaccount']['accrueInterestAmount']))
        print("Account Open Date: {}".format(depositAccount['accountOpenDate']))
        print("Narrative: {}".format(depositAccount['narrative']))
        print("Last Maintenance Officer: {}".format(depositAccount['maintenancehistory']['lastMaintenanceOfficer']))
        print("Last Transaction Branch: {}".format(depositAccount['maintenancehistory']['lastTransactionBranch']))
        print("Maturity Date: {}".format(depositAccount['maturityDate']))
        print("Interest Rate: {}".format(depositAccount['interestRate']))
        print("Officer ID: {}".format(depositAccount['officerID']))
        print("Current Status: {}".format(depositAccount['currentStatus']))
        print("Currency: {}".format(depositAccount['currency']))
        print("Assigned Account For Account Management Fee Deduction: {}".format(depositAccount['assignedAccountForAccountManagementFeeDeduction']))
        print("Compound Interest Rate Basis: {}".format(depositAccount['product']['compoundInterestRateBasis']))
        print("Date Basis For Rate: {}".format(depositAccount['product']['dateBasisForRate']))
        print("Product Name: {}".format(depositAccount['product']['productName']))
        print("Product ID: {}".format(depositAccount['product']['productID']))
        print("Rate Chart Code: {}".format(depositAccount['product']['rateChartCode']))
        print("Balance: {}".format(depositAccount['balance']))
        print("Penalty Rate: {}".format(depositAccount['penaltyRate']))
        print("Home Branch: {}".format(depositAccount['homeBranch']))
        print("Customer ID: {}".format(depositAccount['customerID']))
    elif errorCode == '010041':
        print("OTP has expired.\nYou will receiving a SMS")
    else:
        print(serviceRespHeader['ErrorText'])
    
getDepositAccountDetails()
