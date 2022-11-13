from flask import Blueprint, jsonify, request
import requests
import json
from apis.functions import url, getRecord

requestOTP_api = Blueprint('requestOTP_api', __name__)

"""
request_OTP_url = "http://127.0.0.1:5000/api/requestOTP/"
POST
{
    "userID": "xxx",
    "PIN": "xxx"
}
"""

@requestOTP_api.route('/', methods=['POST'])
def requestOTP():
    userID = request.json['userID']
    PIN = request.json['PIN']
    serviceName = 'requestOTP',

    headerObj = {
        'Header': {
            'userID': userID,
            'PIN': PIN,
            'serviceName': serviceName
        }
    }

    final_url = "{0}?Header={1}".format(url(), json.dumps(headerObj))
    response = requests.post(final_url)

    serviceRespHeader = response.json()['Content']['ServiceResponse']['ServiceRespHeader']
    errorCode = serviceRespHeader['GlobalErrorID']

    if errorCode == '010000':
        return {'message': "OTP Sent"}, 200

    elif errorCode == '010041':
        return {'message': "OTP has expired.\nYou will receiving a SMS"}, 404

    else:
        return {'message': serviceRespHeader['ErrorText']}, 404
