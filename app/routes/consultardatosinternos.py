from fastapi import APIRouter
from app.middleware.token_route import VerifyTokenRoute
import sqlalchemy
import pandas as pd
import json

consultardatos = APIRouter(route_class=VerifyTokenRoute)


@consultardatos.post("/consultardatos")
def consultar():
    conn = sqlalchemy.create_engine("mariadb+pymysql://root:root@mydb/meli?charset=utf8mb4").connect()
    Data = pd.DataFrame()
    Data = pd.read_sql_table(table_name='meliData',con=conn,columns = ['fec_alta', 'user_name','codigo_zip','credit_card_num','direccion','geo_latitud','geo_longitud','color_favorito','foto_dni','ip','auto','auto_modelo','auto_tipo','auto_color','cantidad_compras_realizadas','avatar','fec_birthday','id'])
    jsonRespose=Data.to_json(orient ='records')
    jsonp = json.loads (jsonRespose)
    print(jsonp)
    return jsonp