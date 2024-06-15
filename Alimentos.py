from pydantic import BaseModel
from fastapi import FastAPI

class Alimento:
    def __init__(self, id: int, nome: str, preco: float, disponibilidade: bool, quantidade: int, imagem: str):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.disponibilidade = disponibilidade
        self.quantidade = quantidade
        self.imagem = imagem

