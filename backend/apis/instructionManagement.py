import os
import sys
import json
import requests
from flask import Blueprint, jsonify, request
# from apis.instruction import createInstruction
# from apis.referenceData import billingOrganizations
# from apis.payments import billPayment
# from apis.invokes import invoke_http
# from apis.users import getBankAccount

billPaymentUrl = "http://127.0.0.1:5000/api/payments/billPayment"
refUrl = "http://127.0.0.1:5000/api/referenceData/billingOrganizations/"
directDebit = "http://127.0.0.1:5000/api/payments/directDebit"
emailSuccess = "http://127.0.0.1:5000/api/email_api/sendingEmail/success"
emailFailure = "http://127.0.0.1:5000/api/email_api/sendingEmail/failure"
instruction = "http://127.0.0.1:5000/api/instruction_api/createInstruction"

# This service does creation of instruction which will be sent to GMS
instructionManagement_api = Blueprint('instructionManagement_api', __name__)


@instructionManagement_api.route('/newInstruction', methods=['POST'])
def newInstruction():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            instruction = request.get_json()
            GMSAccountID = instruction['GMSAccountID']  # use 9698
            # bankAccountID = instruction['bankAccountID']
            # 0471
            billingOrganizationAccountID = instruction['billingOrganizationAccountID']
            transactionAmount = instruction['transactionAmount']
            transactionReferenceNumber = instruction['transactionReferenceNumber']
            narrative = instruction['narrative']
            bankac = "http://127.0.0.1:5000/api/users/"
            bankac += GMSAccountID+"/billingOrganizations/"+billingOrganizationAccountID
            print("\nRetrieving bank account")
            x = requests.get(bankac)
            # print(x.status_code)
            if x.status_code == 200:
                # Original Payee account
                bankAccountID = (x.json()['bankAccountID'])
                print(bankAccountID)  # Original Payee account
            else:  # if no associated account, return
                return jsonify({"error": "No valid account found"}), 404

            print("Pull Money from Payee to GMS first")

            data = {

                "userID": "GMS",  # GMS
                "PIN": "123456",
                "OTP": "999999",
                "accountFrom": GMSAccountID,  # GMS
                "accountTo": bankAccountID,  # Bill to customer
                "transactionAmount": transactionAmount,
                "transactionReferenceNumber": transactionReferenceNumber,
                "narrative": narrative
            }
            print("\Processing new instruction:", instruction)
            name = requests.get(refUrl+billingOrganizationAccountID).json()['billingOrgName']
            x = requests.post(directDebit, json=data)
            print(x.status_code)
            if x.status_code == 200:
              
                print("\nRetrieving organization name")

                print("Invoking payment service")  # Pay from GMS to Great Eastern
                data = {
                    "userID": "GMS",
                    "PIN": "123456",
                    "OTP": "999999",
                    "accountFrom": GMSAccountID,  # we are using starhub as GMS. We are paying on behalf
                    "accountTo": billingOrganizationAccountID,  # recipient, eg: Great Eastern
                    "transactionAmount": transactionAmount,
                    "transactionReferenceNumber": transactionReferenceNumber,
                    "narrative": narrative
                }
                x = requests.post(billPaymentUrl, json=data)
                print("Payment Result")
                result = x.status_code
                print(result)
                if result == 200:
                    recordCreation = processInstruction(
                        GMSAccountID, bankAccountID, billingOrganizationAccountID, transactionAmount, transactionReferenceNumber, narrative, 'Success')
                else:
                    recordCreation = processInstruction(
                        GMSAccountID, bankAccountID, billingOrganizationAccountID, transactionAmount, transactionReferenceNumber, narrative, 'Failure')
                if recordCreation:
                    if result == 200:
                        # success
                        print("Invoking Email service")
                        email = processEmailSending(
                            0, GMSAccountID, transactionAmount, narrative, name, transactionReferenceNumber)
                    # else:
                    #     # fail
                    #     failure = processEmailSending(
                    #         1, GMSAccountID, transactionAmount, narrative, name, transactionReferenceNumber)
                    #     if failure:
                    #         return jsonify({
                    #             "code": 404,
                    #             "message": "Instruction record saved and sent email regarding insufficient balance"
                    #         }), 404
                    if email:
                        return jsonify({
                            "code": 200,
                            "message": "Instruction record saved and sent email successfully"
                        }), 200

            else:
                recordCreation = processInstruction(
                GMSAccountID, bankAccountID, billingOrganizationAccountID, transactionAmount, transactionReferenceNumber, narrative, 'Failure')
                failure = processEmailSending(1, GMSAccountID, transactionAmount, narrative, name, transactionReferenceNumber)
                if failure:
                    return jsonify({
                            "code": 404,
                            "message": "Sent email regarding insufficient balance"
                    }), 404

        except Exception as e:
            return jsonify({
                "code": 500,
                "message": "An error has occurred: ",
                "e": e
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "An error has occurred"}), 400


def processInstruction(GMSAccountID, bankAccountID, name, transactionAmount, transactionReferenceNumber, narrative, status):
    print('\n-----Invoking createInstruction microservice-----')
    data = {
                    
                    "GMSAccountID": GMSAccountID, 
                    "bankAccountID": bankAccountID, 
                     "billingOrgName": name,
                    "transactionAmount": transactionAmount,
                    "transactionReferenceNumber": transactionReferenceNumber,
                    "narrative": narrative,
                    "status": status
                }
    x = requests.post(instruction, json=data)
    print(x)
    recordCreation = x.status_code
    if recordCreation == 200:
        return True
    else:
        return False
    


def processEmailSending(res, GMSAccountID, transactionAmount, narrative, billingOrganizationAccountID, transactionReferenceNumber):
    print('\n-----Invoking sendEmail microservice-----')
    if res == 0:  # success
        data = {
                "GMSAccountID": GMSAccountID,  # GMS
                "transactionAmount": transactionAmount,  # Bill to customer
                "narrative": narrative,
                "billingOrganizationAccount": billingOrganizationAccountID,
                "transactionReferenceNumber": transactionReferenceNumber
            }
        x = requests.post(emailSuccess, json=data)
        # result = x.status_code
        print(x)
        result=x.status_code

        # result = sendEmailSuccess(GMSAccountID, transactionAmount, narrative,
        #                           billingOrganizationAccountID, transactionReferenceNumber)
        # print(result)
    else:
        data = {
                "GMSAccountID": GMSAccountID,  # GMS
                "transactionAmount": transactionAmount,  # Bill to customer
                "narrative": narrative,
                "billingOrganizationAccount": billingOrganizationAccountID,
                "transactionReferenceNumber": transactionReferenceNumber
            }
        x = requests.post(emailFailure, json=data)
        # result = x.status_code
        print(x)
        result=x.status_code
    if result == 200:
        return True
    else:
        return False