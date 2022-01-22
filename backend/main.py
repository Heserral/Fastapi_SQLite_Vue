#uvicorn main:app --reload --host 0.0.0.0 --port 5000

#https://testdriven.io/blog/developing-a-single-page-app-with-fastapi-and-vuejs/#handling-unauthorized-users-and-expired-tokens

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from tortoise import Tortoise
from database.register_tortoise import register_tortoise

# enable schemas to read relationship between models
Tortoise.init_models(["database.models"], "models")

from routes import users, notes

app = FastAPI() #docs_url=None,redoc_url=None

#Nosotros arrancamos fastapi en localhost:5000, pero vue develop arranca en localhost:8080. TENEMOS PROBLEMA DE CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"], #aceptamos solo conexiones CORES desde estra otra ip y puerto
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="./static"), name="static")

app.include_router(users.router)
app.include_router(notes.router)

register_tortoise(app, generate_schemas=True)

@app.get("/")
def home():
    return "Hello, World!"
