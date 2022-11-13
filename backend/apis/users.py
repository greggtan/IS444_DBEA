from flask import Blueprint, jsonify, request
import requests, json
from models.shared_model import db
from apis.functions import url,getRecord

from models.UserModel import User
from schemas.UserSchema import UserSchema, UserWithBankAccountsSchema

from models.BankAccountModel import BankAccount
from schemas.BankAccountSchema import BankAccountSchema

from models.UserBillingOrganizationModel import UserBillingOrganization
from schemas.UserBillingOrganizationSchema import UserBillingOrganizationSchema

from models.RequestModel import Request
from schemas.RequestSchema import RequestSchema

users_api = Blueprint('users_api', __name__)

billPaymentUrl = "http://127.0.0.1:5000/api/payments/billPayment"
refUrl = "http://127.0.0.1:5000/api/referenceData/billingOrganizations/"
directDebit = "http://127.0.0.1:5000/api/payments/directDebit"
directDebitAuthorization = "http://127.0.0.1:5000/api/payments/directDebitAuthorization"

#create schema
user_schema = UserSchema()
user_with_bank_accounts_schema = UserWithBankAccountsSchema()

bank_account_schema = BankAccountSchema()
bank_accounts_schema = BankAccountSchema(many=True)

user_billing_organization_schema = UserBillingOrganizationSchema()
user_billing_organizations_schema = UserBillingOrganizationSchema(many=True)

request_schema = RequestSchema()
requests_schema = RequestSchema(many=True)

#Create API to check if GMSAccountID Exist
@users_api.route('/<GMSAccountID>', methods=['GET'])
def checkGMSAccountID(GMSAccountID):
    user = User.query.filter_by(GMSAccountID=GMSAccountID).first()
    if user:
        return user_schema.jsonify(user)
    return jsonify({"error": "Invalid GMS Account ID"}), 401

#Add GMSAccountID
@users_api.route('/', methods=['POST'])
def addGMSAccountID():
    GMSAccountID = request.json['GMSAccountID']
    user = User.query.filter_by(GMSAccountID=GMSAccountID).first()
    if user:
        return user_schema.jsonify(user)
    new_user = User(GMSAccountID)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

#Add Bank Account to user
@users_api.route('/<GMSAccountID>/bankAccounts', methods=['POST'])
def addBankAccount(GMSAccountID):
    bankAccountID = request.json['bankAccountID']

    data = {

            "userID": request.json['userID'], 
            "PIN": request.json['PIN'],
            "OTP": request.json['OTP'],
            "customerAccountID": request.json['bankAccountID'],  
            "billingOrgAccountID": GMSAccountID, 
        }

    res = requests.post(directDebitAuthorization, json=data)

    if res.status_code == 200:
        user = User.query.filter_by(GMSAccountID=GMSAccountID).first()
        if user:
            new_bank_account = BankAccount(bankAccountID, user.GMSAccountID)
            db.session.add(new_bank_account)
            db.session.commit()
            return bank_account_schema.jsonify(new_bank_account)
        return jsonify({"error": "Invalid GMS Account ID"}), 401
    return jsonify({"error": "Invalid account details"}), 401

#Get Bank Accounts of user
@users_api.route('/<GMSAccountID>/bankAccounts', methods=['GET'])
def getBankAccounts(GMSAccountID):
    user = User.query.filter_by(GMSAccountID=GMSAccountID).first()

    if not user:
        return jsonify({"error": "Invalid GMS Account ID"}), 401

    bank_accounts = user.bankAccounts

    bank_accounts_dict = bank_accounts_schema.dump(bank_accounts)
    print(bank_accounts_dict)
    #get billing organization for each bank account
    for i,bank_account in enumerate(bank_accounts):
        bank_accounts_dict[i]['billingOrganizations']=[]
        for user_billing_organization in bank_account.userBillingOrganizations:

            billOrg = requests.get(refUrl+user_billing_organization.billingOrganizationAccountID).json()
            bank_accounts_dict[i]['billingOrganizations'].append(billOrg)

    return jsonify(bank_accounts_dict)

#add billing organization account id to user
@users_api.route('/<GMSAccountID>/billingOrganizations', methods=['POST'])
def addBillingOrganization(GMSAccountID):
    billingOrganizationAccountID = request.json['billingOrganizationAccountID']
    bankAccountID = request.json['bankAccountID']


    

    user = User.query.filter_by(GMSAccountID=GMSAccountID).first()
    #if bank account id is under user
    if user:
        bankAccount = BankAccount.query.filter_by(bankAccountID=bankAccountID, GMSAccountID = GMSAccountID).first()
        # print(bankAccount)
        if bankAccount:
            billingOrganization = requests.get(refUrl+billingOrganizationAccountID).json()
            if billingOrganization['billingOrgName']!="Not found":
                userBillingOrganization = UserBillingOrganization.query.filter_by(billingOrganizationAccountID=billingOrganizationAccountID, GMSAccountID=GMSAccountID).first()
    
                if userBillingOrganization:
                    userBillingOrganization.bankAccountID = bankAccountID
                    db.session.commit()
                    return user_billing_organization_schema.jsonify(userBillingOrganization)
                else:
                    new_user_billing_organization = UserBillingOrganization(billingOrganizationAccountID, GMSAccountID, bankAccountID)
                    db.session.add(new_user_billing_organization)
                    db.session.commit()
                    return user_billing_organization_schema.jsonify(new_user_billing_organization)
            return jsonify({"error": "Invalid Billing Organization Account ID"}), 401
        return jsonify({"error": "Invalid Bank Account ID"}), 401
    return jsonify({"error": "Invalid GMS Account ID"}), 401

#Get billing organization account id of user
@users_api.route('/<GMSAccountID>/billingOrganizations', methods=['GET'])
def getBillingOrganization(GMSAccountID):
    user = User.query.filter_by(GMSAccountID=GMSAccountID).first()
    if user:
        return user_billing_organizations_schema.jsonify(user.userBillingOrganizations)
    return jsonify({"error": "Invalid GMS Account ID"}), 401

#get bank account based on user and billing organization account id pair
@users_api.route('/<GMSAccountID>/billingOrganizations/<billingOrganizationAccountID>', methods=['GET'])
def getBankAccountServingBillOrg(GMSAccountID, billingOrganizationAccountID):
    user = User.query.filter_by(GMSAccountID=GMSAccountID).first()
    if user:
        user_billing_organization = UserBillingOrganization.query.filter_by(billingOrganizationAccountID=billingOrganizationAccountID, GMSAccountID=GMSAccountID).first()
        if user_billing_organization:
            bankAccountID = user_billing_organization.bankAccountID
            bankAccount = BankAccount.query.filter_by(bankAccountID=bankAccountID, GMSAccountID=GMSAccountID).first()
            return bank_account_schema.jsonify(bankAccount)
        return jsonify({"error": "Invalid Billing Organization Account ID"}), 401
    return jsonify({"error": "Invalid GMS Account ID"}), 401

#get ALL transaction history of user bankAccount pair from request table
@users_api.route('/<GMSAccountID>/bankAccounts/<bankAccountID>/transactions', methods=['GET'])
def getTransactions(GMSAccountID, bankAccountID):
    user = User.query.filter_by(GMSAccountID=GMSAccountID).first()
    if user:
        bankAccount = BankAccount.query.filter_by(bankAccountID=bankAccountID, GMSAccountID=GMSAccountID).first()
        if bankAccount:
            transactions = Request.query.filter_by(bankAccountID=bankAccountID, GMSAccountID=GMSAccountID).all()
            return requests_schema.jsonify(transactions)
