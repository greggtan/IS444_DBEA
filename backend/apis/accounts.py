
from flask import Blueprint, jsonify, request
import requests, json
from apis.functions import url,getRecord

accounts_api = Blueprint('accounts_api', __name__)

#Get Deposit Account Details
@accounts_api.route('/getDepositAccountDetails', methods=['POST'])
def getDepositAccountDetails():
    #Header
    serviceName = 'getDepositAccountDetails'
    userID = request.json['userID']
    PIN = request.json['PIN']
    OTP = request.json['OTP']
    #Content
    accountID = request.json['accountID']
    
    
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
        return jsonify(depositAccount)
    elif errorCode == '010041':
        # print("OTP has expired.\nYou will receiving a SMS")
        return jsonify({"error":"OTP has expired.\nYou will receiving a SMS"}),401
    else:
        # print(serviceRespHeader['ErrorText'])
        return jsonify({"error":serviceRespHeader['ErrorText']}),500

#Get Deposit Account Balance
@accounts_api.route('/getDepositAccountBalance', methods=['POST'])
def getDepositAccountBalance():
    #Header
    serviceName = 'getDepositAccountBalance'
    userID = request.json['userID']
    PIN = request.json['PIN']
    OTP = request.json['OTP']
    #Content
    accountID = request.json['accountID']
    
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
        # print("Balance: {}".format(DepositAccount['balance']))
        return jsonify(DepositAccount)
    elif errorCode == '010041':
        return jsonify({"error":"OTP has expired.\nYou will receiving a SMS"}),401
    else:
        return jsonify({"error":serviceRespHeader['ErrorText']}),500