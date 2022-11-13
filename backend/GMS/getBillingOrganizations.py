from pprint import pprint
import requests, json
from functions import url


def getBillingOrganizations(accID):
    serviceName = 'getBillingOrganizations'
    headerObj = {
                        'Header': {
                        'serviceName': serviceName,
                        'userID': '',
                        'PIN': '',
                        'OTP': ''
                        }
                        }
    final_url="{0}?Header={1}".format(url(),json.dumps(headerObj))
    response = requests.post(final_url)
    
    types = response.json()['Content']['ServiceResponse']['BillingOrgList']['BillingOrg']
    ID_List= []
    Name_List = []
    # print(types)
    for i in range(len(types)):
        billingOrg = types[i]
        ID_List.append(billingOrg['AccountID'])
        Name_List.append(billingOrg['BillingOrgName'])
    # print(Name_List)
    # print(ID_List)
    if accID in ID_List:
        index = ID_List.index(accID)
        # pprint( Name_List[index])
        
        return Name_List[index]
    else:
        # print('Account ID not found')
        return 'Not found'
    

# getBillingOrganizations("0000009698")