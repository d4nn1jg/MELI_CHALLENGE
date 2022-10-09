from fastapi import FastAPI
import database
from consultarJson import *
from dotenv import load_dotenv
from routes.auth import auth_routes
from routes.consultardatosinternos import consultardatos
from routes.cargardatos import cargar_datos

app = FastAPI()

app.include_router(cargar_datos,prefix="/api")
app.include_router(auth_routes,prefix="/api")
app.include_router(consultardatos, prefix="/api")
load_dotenv ()

@app.get("/cargarDatos")
def read_getUser():
    datosRaw = consultarWebService()
    dataJson = parsearJson(datosRaw)
    dataModified = modifyData(dataJson)
    dataframe = jsontopanda(dataModified)
    conn = database.connDB()
    print(dataframe)
    dataframe.to_sql("meliData",con=conn,if_exists="replace")
    result= "OK"
    return result



@app.get("/")
def read_root():
    return {"Version": "1.0"} 