from pydantic import BaseModel, Field #type: ignore
from typing import Optional

class Pedido(BaseModel):
    id: Optional[int] = None
    mesa: int = Field(..., gt=0, description="A mesa deve ser maior que zero")
    
    # Adicionamos o 'pattern' para aceitar apenas letras e espaços
    cliente: str = Field(..., min_length=2, pattern=r"^[a-zA-ZÀ-ÿ\s]+$", description="Nome deve conter apenas letras")
    
    item: str = Field(..., min_length=2)
    preco: float = Field(..., gt=0, description="O preço não pode ser negativo")
    status: str = "Pendente"