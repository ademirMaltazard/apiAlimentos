from fastapi import FastAPI
from BancoDados import bd
from Alimentos import ModelAlimento

app = FastAPI()

@app.get("/alimentos/")
def BuscarTodosAlimentos():
    return bd.getAlimentos()


@app.get("/alimentos/{id}")
def BuscarUmAlimento(id: int):
    return bd.getAlimento(id)

@app.post("/alimentos/cadastrar/")
def CadastrarAlimento(alimento: ModelAlimento):
    return bd.setAlimento(alimento)

@app.put("/alimentos/atualizar/")
def AtualizarAlimento(alimento: ModelAlimento):
    return bd.putAlimento(alimento)

@app.delete("/alimentos/delete/{id}")
def DeletarUmAlimento(id: int):
    return bd.deleteAlimento(id)

@app.put("alimentos/atualizar/")
def AtualizarAlimento(alimento: ModelAlimento):
    return bd.putAlimento(alimento)
