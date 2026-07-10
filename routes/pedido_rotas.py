from fastapi import APIRouter, Depends, HTTPException, Header #type: ignore
from models.pedido import Pedido #type: ignore
from models.cardapio import ItemCardapio  #type: ignore
from services import pedido_service #type: ignore

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

def verificar_token(x_token: str = Header(default=None)):
    if x_token != "aure-token-123":
        raise HTTPException(status_code=401, detail="Acesso não autorizado. Token inválido.")

@router.get("/")
def listar_pedidos():
    return pedido_service.listar_todos()

@router.post("/", dependencies=[Depends(verificar_token)])
def criar_pedido(pedido: Pedido):
    return pedido_service.criar(pedido)

@router.put("/{pedido_id}", dependencies=[Depends(verificar_token)])
def atualizar_pedido(pedido_id: int, pedido: Pedido):
    atualizado = pedido_service.atualizar(pedido_id, pedido)
    if not atualizado:
        raise HTTPException(status_code=404, detail="Pedido não encontrado na base de dados")
    return atualizado

@router.delete("/cardapio/{item_id}", tags=["Cardapio"])
def deletar_item(item_id: int):
    print(f"DEBUG: Tentando deletar item ID: {item_id}") 
    sucesso = pedido_service.deletar_item_cardapio(item_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return {"mensagem": "Item removido do cardápio"}

from services import pedido_service #type: ignore

@router.post("/cardapio", tags=["Cardapio"])
def criar_item_cardapio(item: ItemCardapio):
    pedido_service.adicionar_ao_cardapio(item.nome, item.preco)
    return {"mensagem": f"O prato '{item.nome}' foi adicionado ao cardápio!"}

@router.get("/cardapio", tags=["Cardapio"])
def obter_cardapio():
    return pedido_service.listar_cardapio()

@router.post("/cardapio/popular", tags=["Cardapio"])
def popular_cardapio_teste():
    pedido_service.adicionar_ao_cardapio("Bife Acebolado", 69.99)
    pedido_service.adicionar_ao_cardapio("Coca-Cola 2L", 14.50)
    pedido_service.adicionar_ao_cardapio("Batata Frita", 25.00)
    return {"msg": "Cardápio atualizado!"}

@router.put("/cardapio/{item_id}", tags=["Cardapio"])
def atualizar_item(item_id: int, item: ItemCardapio):
    sucesso = pedido_service.atualizar_item_cardapio(item_id, item.nome, item.preco)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return {"mensagem": "Item atualizado!"}

# ROTAS DE PEDIDOS

@router.delete("/{pedido_id}", dependencies=[Depends(verificar_token)])
def deletar_pedido(pedido_id: int):
    deletado = pedido_service.deletar(pedido_id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return {"mensagem": f"Pedido {pedido_id} deletado com sucesso"}

# ROTAS DE CARDÁPIO 

@router.delete("/cardapio/{item_id}", tags=["Cardapio"])
def deletar_item(item_id: int):
    sucesso = pedido_service.deletar_item_cardapio(item_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return {"mensagem": "Item removido do cardápio"}