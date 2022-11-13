import requests, json
from flask import Blueprint, jsonify, request
from apis.functions import url
import os

from dotenv import load_dotenv

email_api = Blueprint('email_api', __name__)
#Happy Path, Payment Confirmed
@email_api.route('/sendingEmail/success', methods=['POST'])
def sendEmailSuccess():
    #Header
    load_dotenv()
    serviceName = 'sendEmail'
    userID = os.getenv('RETAIL_USER_ID')
    PIN = os.getenv('RETAIL_USER_PIN')
    OTP = os.getenv('RETAIL_OTP')

    GMSAccountID = request.json['GMSAccountID']
    transactionAmount = request.json['transactionAmount']
    narrative = request.json['narrative']
    billingOrganizationAccount = request.json['billingOrganizationAccount']
    transactionReferenceNumber = request.json['transactionReferenceNumber']

    #Content
    emailAddress = 'ystan98@hotmail.com'
    emailSubject = 'Giro Management Service Successful Payment '
    emailBody = ''
    recipient_org = billingOrganizationAccount
    print(recipient_org)
    emailBody ="Thank you for being a loyal customer to Giro Management Service.\nHere is the record of your latest transaction details:"
    emailBody+= "\n \nTransaction Reference ID: " +str(transactionReferenceNumber)+"\nAmount of $" + str(transactionAmount) + " has been successfully paid to " +recipient_org+" for your purchase of " + narrative



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
                        'emailAddress': emailAddress,
                        'emailSubject': emailSubject,
                        'emailBody': emailBody
                        }
                        }
    
    final_url="{0}?Header={1}&Content={2}".format(url(),json.dumps(headerObj),json.dumps(contentObj))
    response = requests.post(final_url)
    serviceRespHeader = response.json()['Content']['ServiceResponse']['ServiceRespHeader']
    errorCode = serviceRespHeader['GlobalErrorID']
    
    if errorCode == '010000':
        print("Email sent")
        return jsonify({"code":200}),200
    elif errorCode == '010041':
        print("OTP has expired.\nYou will receiving a SMS")
        return jsonify({"code":404}),404
    else:
        print(serviceRespHeader['ErrorText'])
        return jsonify({"code":404}),404


#Negative Path, Payment Failed
@email_api.route('/sendingEmail/failure', methods=['POST'])
def sendEmailFailure():
    #Header
    load_dotenv()
    serviceName = 'sendEmail'
    userID = os.getenv('RETAIL_USER_ID')
    PIN = os.getenv('RETAIL_USER_PIN')
    OTP = os.getenv('RETAIL_OTP')


    GMSAccountID = request.json['GMSAccountID']
    transactionAmount = request.json['transactionAmount']
    narrative = request.json['narrative']
    billingOrganizationAccount = request.json['billingOrganizationAccount']
    transactionReferenceNumber = request.json['transactionReferenceNumber']


    #Content
    emailAddress = 'ystan98@hotmail.com'
    emailSubject = 'Giro Management Service Unsuccessful Payment '
    emailBody = ''
    recipient_org = billingOrganizationAccount
    emailBody ="Thank you for being a loyal customer to Giro Management Service.\nWe regret to inform you that your latest GIRO transaction has failed due to insufficient balance. The details are given as:"
    emailBody+= "\n \nTransaction Reference ID: " +str(transactionReferenceNumber)+"\nAmount of $" + str(transactionAmount) + " has failed to pay to " +recipient_org+" for your purchase of " + narrative +' due to insufficient balance in bank account'



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
                        'emailAddress': emailAddress,
                        'emailSubject': emailSubject,
                        'emailBody': emailBody
                        }
                        }
    
    final_url="{0}?Header={1}&Content={2}".format(url(),json.dumps(headerObj),json.dumps(contentObj))
    response = requests.post(final_url)
    serviceRespHeader = response.json()['Content']['ServiceResponse']['ServiceRespHeader']
    errorCode = serviceRespHeader['GlobalErrorID']
    
    if errorCode == '010000':
        print("Email sent")
        return jsonify({"code":200}),200
    elif errorCode == '010041':
        print("OTP has expired.\nYou will receiving a SMS")
        return jsonify({"code":404}),404
    else:
        print(serviceRespHeader['ErrorText'])
        return jsonify({"code":404}),404



