from fastapi import FastAPI # type: ignore
from fastapi.middleware.cors import CORSMiddleware #type:ignore
from pydantic import BaseModel # type: ignore

app = FastAPI(openai_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Pedido(BaseModel):
    id: int
    mesa:int
    cliente:str
    item: str
    preco: float
    status:str = "Pendente"

db_pedidos=[]

@app.get("/pedidos")
def listar_pedidos():
    return db_pedidos

@app.post("/pedidos")
def criar_pedido(pedido: Pedido):
    db_pedidos.append(pedido)
    return {"Mesagem": "Pedido criado!", "pedido": pedido}