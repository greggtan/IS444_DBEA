import requests, json
from functions import url
import os
from dotenv import load_dotenv
def sendEmail(customer_id, amount, item, recipient_org):
    #Header
    load_dotenv()
    serviceName = 'sendEmail'
    userID = os.getenv('RETAIL_USER_ID')
    PIN = os.getenv('RETAIL_USER_PIN')
    OTP = os.getenv('RETAIL_OTP')

    #Content
    emailAddress = 'ystan98@hotmail.com'
    emailSubject = 'Giro Management Service Successful Payment '
    emailBody = ''

    transaction_id= 1210 #to be dynamic later
    transaction_amount = 200.24 #to be dynamic later
    purchase_description = "Diapers" #to be dynamic later
    recipient_org ='Koufu' #to be dynamic later
    emailBody ="Thank you for being a loyal customer to Giro Management Service.\nHere is the record of your latest transaction details:"
    emailBody+= "\n \nTransaction ID: " +str(transaction_id)+"\nAmount of $" + str(transaction_amount) + " has been successfully paid to " +recipient_org+" for your purchase of " + purchase_description




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
    elif errorCode == '010041':
        print("OTP has expired.\nYou will receiving a SMS")
    else:
        print(serviceRespHeader['ErrorText'])

sendEmail()
