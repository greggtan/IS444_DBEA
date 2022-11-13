from flask import Blueprint, jsonify, request
from models.RequestModel import Request
from schemas.RequestSchema import RequestSchema
from models.shared_model import db
# This service does creation of instruction which will be sent to GMS
instruction_api = Blueprint('instruction_api', __name__)

#create schema
request_schema = RequestSchema()

# Creating a new instruction/billing record
#From_acc refers to billing org
@instruction_api.route('/createInstruction', methods=['POST'])
def createInstruction():
    GMSAccountID = request.json['GMSAccountID']
    bankAccountID = request.json['bankAccountID']
    billingOrgName = request.json['billingOrgName']
    transactionAmount = request.json['transactionAmount']
    transactionReferenceNumber = request.json['transactionReferenceNumber']
    narrative = request.json['narrative']  
    status = request.json['status']
    # Create record of instruction in database
    try:
        print("Creating new instruction request")
        rec = Request(GMSAccountID,bankAccountID,billingOrgName,transactionAmount,transactionReferenceNumber,narrative,status)
        print(rec)
        db.session.add(rec)
        db.session.commit()        
        print("New instruction request created successfully")
        return jsonify(
                    {
                        "code": 200,
                        "message": "Created record!"
                    }
                ), 200
    except Exception as e:
                print(e)
                return jsonify(
                    {
                        "code": 500,
                        "message": "An error occurred creating the instruction."
                    }
                ), 500