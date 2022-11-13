import requests
import json
from apis.functions import url, getRecord
from apis.getProductTypes import getProductTypes
from flask import Blueprint, jsonify, request

getCustomerAccounts_api = Blueprint('getCustomerAccounts_api', __name__)


@getCustomerAccounts_api.route('/', methods=['GET'])
def getCustomerAccounts():
    serviceName = 'getCustomerAccounts'
    userID = request.json['userID']
    PIN = request.json['PIN']
    OTP = request.json['OTP'] if 'OTP' in request.json else '999999'

    headerObj = {
                    'Header': {
                        'serviceName': serviceName,
                        'userID': userID,
                        'PIN': PIN,
                        'OTP': OTP
                    }
                }
    final_url = "{0}?Header={1}".format(url(), json.dumps(headerObj))
    response = requests.post(final_url)

    serviceRespHeader = response.json(
    )['Content']['ServiceResponse']['ServiceRespHeader']
    errorCode = serviceRespHeader['GlobalErrorID']

    if errorCode == '010000':
        acc_list = response.json()['Content']['ServiceResponse']['AccountList']
        if acc_list == {}:
            print("No record found!")
        else:
            acc_list = acc_list['account']
            recordCount = getRecord(acc_list)
            output = []

            if recordCount > 1:
                for i in range(0, recordCount, 1):
                    account = acc_list[i]
                    acc_type = getProductTypes(account['productID'])

                    output.append({
                        'Balance': account['balance'],
                        'Account_ID': account['accountID'],
                        'Account_Open_Date': account['accountOpenDate'],
                        'Home_Branch': account['homeBranch'],
                        'Last_Maintenance_Officer': account['maintenancehistory']['lastMaintenanceOfficer'],
                        'Last_Transaction_Branch': account['maintenancehistory']['lastTransactionBranch'],
                        'Parent_Account_Flag': account['parentAccountFlag'],
                        'Interest_Rate': account['interestRate'],
                        'Product_Type': acc_type,
                        'Current_Status': account['currentStatus'],
                        'Officer_ID': account['officerID'],
                        'Currency': account['currency']
                    })
            elif recordCount == 0:
                acc_type=getProductTypes(acc_list['productID'])
                output.append({
                        'Balance': acc_list['balance'],
                        'Account_ID': acc_list['accountID'],
                        'Account_Open_Date': acc_list['accountOpenDate'],
                        'Home_Branch': acc_list['homeBranch'],
                        'Last_Maintenance_Officer': acc_list['maintenancehistory']['lastMaintenanceOfficer'],
                        'Last_Transaction_Branch': acc_list['maintenancehistory']['lastTransactionBranch'],
                        'Parent_Account_Flag': acc_list['parentAccountFlag'],
                        'Interest_Rate': acc_list['interestRate'],
                        'Product_Type': acc_type,
                        'Current_Status': acc_list['currentStatus'],
                        'Officer_ID': acc_list['officerID'],
                        'Currency': acc_list['currency']
                    })
            return jsonify({'Accounts': output}), 200
    elif errorCode == '010041':
        return jsonify({'message': "OTP has expired.\nYou will receiving a SMS"}), 404
    else:
        return jsonify({'message': serviceRespHeader['ErrorText']}), 404
