from flask import Blueprint, jsonify, request
import requests, json
from apis.functions import url,getRecord

billPaymentUrl = "http://127.0.0.1:5000/api/payments/billPayment"
refUrl = "http://127.0.0.1:5000/api/referenceData/billingOrganizations/"
directDebit = "http://127.0.0.1:5000/api/payments/directDebit"

payments_api = Blueprint('payments_api', __name__)

#authorize direct debit between 2 accounts
@payments_api.route('/directDebitAuthorization', methods=['POST'])
def directDebitAuthorization():
    #Header
    serviceName = 'directDebitAuthorization'
    userID = request.json['userID']
    PIN = request.json['PIN']
    OTP = request.json['OTP']
    #Content
    customerAccountID = request.json['customerAccountID']
    billingOrgAccountID = request.json['billingOrgAccountID']

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
        return jsonify({"directDebitAuthorizationID":ServerResponse['DirectDebitAuthorizationID']['_content_']})
    elif errorCode == '010041':
        return jsonify({"error":"OTP has expired.\nYou will receiving a SMS"}),401
    else:
        return jsonify({"error":serviceRespHeader['ErrorText']}),500

#direct debit from customer account to billing organization account
@payments_api.route('/directDebit', methods=['POST'])
def directDebit():
    #Header 
    #Should be GMS account details
    serviceName = 'directDebit'
    userID = request.json['userID'] 
    PIN = request.json['PIN']
    OTP = request.json['OTP']

    #Content
    accountFrom = request.json['accountFrom'] #GIRO instruction from GMS account
    accountTo = request.json['accountTo'] #Giro instruction to user bank account
    transactionAmount = request.json['transactionAmount']
    transactionReferenceNumber = request.json['transactionReferenceNumber']
    narrative = request.json['narrative']

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
        #return transaction ID, balance before and after
        return jsonify({
            "transactionID":ServerResponse['TransactionID']['_content_'],
            "balanceBefore":ServerResponse['BalanceBefore']['_content_'],
            "balanceAfter":ServerResponse['BalanceAfter']['_content_']
            })
    elif errorCode == '010041':
        return jsonify({"error":"OTP has expired.\nYou will receiving a SMS"}),401
    else:
        return jsonify({"error":serviceRespHeader['ErrorText']}),500

#get direct debit authorization list
@payments_api.route('/getDirectDebitAuthorizationList', methods=['POST'])
def getDirectDebitAuthorizationList():
    #Header
    serviceName = 'getDirectDebitAuthorizationList'
    userID = request.json['userID']
    PIN = request.json['PIN']
    OTP = request.json['OTP']
    #Content
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
            return jsonify({"error":"No record found!"}),404
        else:
            dda_list = dda_list['Authorization']
            recordCount = getRecord(dda_list)
            # directDebitAuthorizationList=[]
            if recordCount>1:                 
                for i in range(0,recordCount,1):
                    #camelcase each key in dda_list[i]
                    # print(getBillingOrganizationByID(dda_list[i]['BillingOrgAccountID']).json["billingOrgName"])
                    billingOrganizationAccountID = dda_list[i]['BillingOrgAccountID']
                    name = requests.get(refUrl+billingOrganizationAccountID).json()['billingOrgName']
                    dda_list[i]['billingOrganization'] = name
                    dda_list[i] = {k[0].lower() + k[1:]: v for k, v in dda_list[i].items()}
                return jsonify(dda_list)
            elif recordCount == 0:
                billingOrganizationAccountID = dda_list[i]['BillingOrgAccountID']
                name = requests.get(refUrl+billingOrganizationAccountID).json()['billingOrgName']
                dda_list['billingOrganization'] = name
                dda_list = {k[0].lower() + k[1:]: v for k, v in dda_list.items()}
                return jsonify([dda_list])
    elif errorCode == '010041':
        return jsonify({"error":"OTP has expired.\nYou will receiving a SMS"}),401
    else:
        return jsonify({"error":serviceRespHeader['ErrorText']}),500

#Bill payment api
@payments_api.route('/billPayment', methods=['POST'])
def billPayment():
    #Header
    serviceName = 'billPayment'
    userID = request.json['userID']
    PIN = request.json['PIN']
    OTP = request.json['OTP']
    #Content
    accountFrom = request.json['accountFrom']
    accountTo = request.json['accountTo']
    transactionAmount = request.json['transactionAmount']
    transactionReferenceNumber = request.json['transactionReferenceNumber']
    narrative = request.json['narrative']
    
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
        return jsonify({
            "transactionID":ServerResponse['TransactionID']['_content_'],
            "balanceBefore":ServerResponse['BalanceBefore']['_content_'],
            "balanceAfter":ServerResponse['BalanceAfter']['_content_']
            })
    elif errorCode == '010041':
        return jsonify({"error":"OTP has expired.\nYou will receiving a SMS"}),401
    else:
        return jsonify({"error":serviceRespHeader['ErrorText']}),500