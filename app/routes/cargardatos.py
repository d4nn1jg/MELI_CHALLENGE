from fastapi import APIRouter
import app.database
from app.consultarJson import *


cargar_datos = APIRouter()

@cargar_datos.get("/cargardatos")
def read_getUser():
    datosRaw = consultarWebService()
    dataJson = parsearJson(datosRaw)
    dataModified = modifyData(dataJson)
    dataframe = jsontopanda(dataModified)
    conn = app.database.connDB()
    print(dataframe)
    dataframe.to_sql("meliData",con=conn,if_exists="replace")
    result= "OK"
    return result