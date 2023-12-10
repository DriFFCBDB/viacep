from fastapi import FastAPI

import requests

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get-cep/")
async def get_cep(cep: str):

    resposta = requests.get("https://viacep.com.br/ws/" + cep + "/xml/")

    return { 
        "resposta":resposta.text
    }