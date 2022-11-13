from flask import request, jsonify
from flask_cors import CORS
from flask import Flask

from werkzeug.exceptions import HTTPException, BadRequest

#create database
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

#get db and ma
from models.shared_model import db
from schemas.shared_model import ma

from models.UserModel import User
from models.BankAccountModel import BankAccount
from models.UserBillingOrganizationModel import UserBillingOrganization
from models.RequestModel import Request

from apis.payments import payments_api
from apis.accounts import accounts_api
from apis.instructionManagement import instructionManagement_api
from apis.instruction import instruction_api
from apis.sendingEmail import email_api
from apis.referenceData import reference_data_api
from apis.users import users_api
from apis.stocks import stocks_api
from apis.requestOTP import requestOTP_api
from apis.getCustomerAccounts import getCustomerAccounts_api
from apis.exchangerate import exchange_rate_api

import os
from dotenv import load_dotenv
load_dotenv(".env")


# Get database address.
db_addr = "localhost"
# Get username of the database.
db_user = "root"
# Get password.
PASS = os.getenv("DB_PASSWORD") 
if not PASS:
    PASS = ""
db_pass = PASS
# Get the database name.
db_name = "dbea"
# join the inputs into a complete database url.
db_url = f"mysql+mysqlconnector://{db_user}:{db_pass}@{db_addr}/{db_name}"

# Create an engine object.
engine = create_engine(db_url, echo=True)

# Create database if it does not exist.
if not database_exists(engine.url):
    create_database(engine.url)
    print("Database created.")


#create Flask app  
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#handle CORS
CORS(app)

#Create Tables
with app.app_context():
    db.init_app(app)
    db.create_all()
    ma.init_app(app)

    #add a user to the database
    if not User.query.filter_by(GMSAccountID="9907").first():
        new_user = User("9907")
        db.session.add(new_user)
        db.session.commit()

def handle_error(error):
    code = 500
    
    if isinstance(error, KeyError):
        code = 400  
        error =  "Missing input: "+str(error) 
    elif isinstance(error, HTTPException):
        code = error.code
        if isinstance(error, BadRequest):
            error =  "Missing Body or invalid JSON syntax"

    return jsonify(message= str(error)), code

#register database error handler
app.register_error_handler(Exception, handle_error)

#Register API route/blueprint
app.register_blueprint(payments_api, url_prefix='/api/payments')
app.register_blueprint(accounts_api, url_prefix='/api/accounts')
app.register_blueprint(instructionManagement_api, url_prefix='/api/instructionManagement')
app.register_blueprint(instruction_api, url_prefix='/api/instruction_api')
app.register_blueprint(reference_data_api, url_prefix='/api/referenceData')
app.register_blueprint(users_api, url_prefix='/api/users')
app.register_blueprint(email_api, url_prefix='/api/email_api')
app.register_blueprint(requestOTP_api, url_prefix='/api/requestOTP')
app.register_blueprint(stocks_api, url_prefix='/api/stocks')

#run app
if __name__ == '__main__':
    app.run(debug=True)




