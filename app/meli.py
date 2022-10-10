from fastapi import FastAPI
from app.consultarJson import *
from dotenv import load_dotenv
from app.routes.auth import auth_routes
from app.routes.consultardatosinternos import consultardatos
from app.routes.cargardatos import cargar_datos

app = FastAPI()

app.include_router(cargar_datos,prefix="/api")
app.include_router(auth_routes,prefix="/api")
app.include_router(consultardatos, prefix="/api")
load_dotenv ()


@app.get("/")
def read_root():
    return {"Version": "1.0"} 