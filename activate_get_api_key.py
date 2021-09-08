#This code is an extraction from Simon Light repository in GitHub
#https://github.com/SimonLight001/COVID-Entry-Exit-system

#Important to install the library PyJWT not the jwt
#pip install PyJWT requests pprint json socket

import jwt
import requests
from pprint import pprint
import json
import os


def get_API_Key_and_auth():

    # Gets public key from spaces and places in correct format
    print("-- No API Key Found --")
    pubKey = requests.get(
        'https://partners.dnaspaces.io/client/v1/partner/partnerPublicKey/')
    pubKey = json.loads(pubKey.text)
    pubKey = pubKey['data'][0]['publicKey']
    pubKey = '-----BEGIN PUBLIC KEY-----\n' + pubKey + '\n-----END PUBLIC KEY-----'

    print ("pubkey:")
    print ('\n',pubKey,'\n')

    # Gets user to paste in generated token from app
    token = input('Enter token here: ')

    # Decodes JSON Web Token to get JSON out
    decodedJWT = jwt.decode(token, pubKey, algorithms=["RS256"])
    decodedJWT = json.dumps(decodedJWT, indent=2)
    print('\n',decodedJWT,'\n')

    # picks up required values out of JWT
    decodedJWTJSON = json.loads(decodedJWT)
    appId = decodedJWTJSON['appId']
    activationRefId = decodedJWTJSON['activationRefId']

    # creates payloads and headers ready to activate app
    authKey = 'Bearer ' + token
    payload = {'appId': appId, 'activationRefId': activationRefId}
    header = {'Content-Type': 'application/json', 'Authorization': authKey}

    # Sends request to spaces with all info about JWT to confirm its correct, if it is,
    #the app will show as activated

    activation = requests.post(
        'https://partners.dnaspaces.io/client/v1/partner/activateOnPremiseApp/', headers=header, json=payload)

    activation = json.loads(activation.text)
    print(activation['message'])
    print('Your API key is stored at the API_KEY.txt file')
    apiKey = activation['data']['apiKey']

    f = open("API_KEY.txt", "a")
    f.write(apiKey)
    f.close()
    return apiKey


try:
    if os.stat("API_KEY.txt").st_size > 0:
        f = open("API_KEY.txt")
        apiKey = f.read()
        f.close()
        print("-- API Key Found -- ")
        print("-- If you wanted to renew your API key, just delete the file API_KEY.txt --")
    else:
        apiKey = get_API_Key_and_auth()
except:
    apiKey = get_API_Key_and_auth()
