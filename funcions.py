from jwt import encode, decode
from jwt import exceptions
from datetime import datetime, timedelta
from os import getenv
from fastapi.responses import JSONResponse
import sqlalchemy
import pandas as pd
import json

def read_allData():
    conn = sqlalchemy.create_engine("mariadb+pymysql://root:root@127.0.0.1/meli?charset=utf8mb4").connect()
    Data = pd.DataFrame()
    Data = pd.read_sql_table(table_name='meliData',con=conn,columns = ['fec_alta', 'user_name','codigo_zip','credit_card_num','direccion','geo_latitud','geo_longitud','color_favorito','foto_dni','ip','auto','auto_modelo','auto_tipo','auto_color','cantidad_compras_realizadas','avatar','fec_birthday','id'])
    jsonRespose=Data.to_json(orient ='records')
    jsonp = json.loads (jsonRespose)
    print(jsonp)
    return jsonp

def expire_date(days:int):
    date = datetime.now()
    newdate = date + timedelta(days)
    return newdate

def write_token(data:dict):
    token = encode(payload = {**data,"exp": expire_date(2)}, key = getenv("SECRET"), algorithm = "HS256")
    return token

def validate_token(token, output = False):   
    try:
        if output:
           return decode(token, key = getenv("SECRET"), algorithms=["HS256"])
        decode(token, key = getenv("SECRET"), algorithms=["HS256"])
    except exceptions.DecodeError:
        return JSONResponse(content={"message" : "Invalind Token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message" : "Token Expired"}, status_code=401)


    