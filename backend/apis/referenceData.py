from flask import Blueprint, jsonify, request
import requests, json
from apis.functions import url,getRecord

reference_data_api = Blueprint('reference_data_api', __name__)

# Get billing organizations.
@reference_data_api.route('/billingOrganizations', methods=['GET'])
def getBillingOrganizations():
    serviceName = 'getBillingOrganizations'
    headerObj = {
        'Header': {
            'serviceName': serviceName,
            'userID': '',
            'PIN': '',
            'OTP': ''
        }
    }
    final_url = "{0}?Header={1}".format(url(), json.dumps(headerObj))
    response = requests.post(final_url)

    types = response.json()[
        'Content']['ServiceResponse']['BillingOrgList']['BillingOrg']
    
    for i in range(len(types)):
        types[i] = {k[0].lower() + k[1:]: v for k, v in types[i].items()}

    return jsonify(types)

#Get a single billing organization.
@reference_data_api.route('/billingOrganizations/<accID>', methods=['GET'])
def getBillingOrganizationByID(accID):
    serviceName = 'getBillingOrganizations'
    headerObj = {
        'Header': {
            'serviceName': serviceName,
            'userID': '',
            'PIN': '',
            'OTP': ''
        }
    }
    final_url = "{0}?Header={1}".format(url(), json.dumps(headerObj))
    response = requests.post(final_url)

    types = response.json()[
        'Content']['ServiceResponse']['BillingOrgList']['BillingOrg']
    ID_List= []
    Name_List = []

    #convert types keys to camel case
    for i in range(len(types)):
        billingOrg = types[i]
        ID_List.append(billingOrg['AccountID'])
        Name_List.append(billingOrg['BillingOrgName'])
        types[i] = {k[0].lower() + k[1:]: v for k, v in types[i].items()}
    # print(Name_List)
    # print(ID_List)
    accID = accID.zfill(10)
    if accID in ID_List:
        index = ID_List.index(accID)
        
        return jsonify(types[index])
    else:
        # print('Account ID not found')
        return jsonify({"billingOrgName":'Not found'})
