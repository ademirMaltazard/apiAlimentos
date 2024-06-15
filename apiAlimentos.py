from fastapi import FastAPI
from BancoDados import bd
from Alimentos import ModelAlimento

app = FastAPI()

@app.get("/alimentos/")
def BuscarTodosAlimentos():
    resposta = bd.getAlimentos()
    return {
        "message": resposta,
        "statusCode": 200
    }

@app.get("/alimentos/{id}")
def BuscarUmAlimento(id: int):
    return bd.getAlimento(id)

@app.post("/alimentos/cadastrar/")
def CadastrarAlimento(alimento: ModelAlimento):
    return bd.setAlimento(alimento)