import requests
import pandas as pd
import json
from cryptography.fernet import Fernet


key = Fernet.generate_key()

def consultarWebService():
    url = "https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios"
    jsonInfo = requests.get(url)
    datosResponse = jsonInfo.text
    return datosResponse

def parsearJson(datos):
    jsonResponse= json.loads(datos)
    return jsonResponse

def jsontopanda(jsonInfo):
    #data = json.loads(jsonInfo)
    df = pd.DataFrame(jsonInfo)
    return df

def stringEncrypt(message,key):
    fernet = Fernet(key)
    encMessage = fernet.encrypt(message.encode())
    return encMessage

def unencryptString(ecMessage,key):
    fernet = Fernet(key)
    decMessage = fernet.decrypt(ecMessage).decode()
    return decMessage


def modifyData(dataJson):
    length=len(dataJson)
    #print(length)
    for i in range(0,length,1):
        #dataJson[0]["user_name"]= "prueba"
        temp = dataJson[i]["credit_card_num"]
        dataJson[i]["credit_card_num"] = stringEncrypt(temp,key)
        dataJson[i]["credit_card_ccv"] = "***"
        #print(dataJson[i]["credit_card_num"])
        #print(dataJson[i]["credit_card_ccv"])
    return dataJson
