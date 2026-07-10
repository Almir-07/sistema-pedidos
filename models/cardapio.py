from pydantic import BaseModel #type: ignore

class ItemCardapio(BaseModel):
    nome: str
    preco: float

def atualizar_item_cardapio(item_id: int, nome: str, preco: float):
    conn = get_conexao() #type: ignore
    cursor = conn.execute("UPDATE cardapio SET nome = ?, preco = ? WHERE id = ?", (nome, preco, item_id))
    linhas_afetadas = cursor.rowcount
    conn.commit()
    conn.close()
    return linhas_afetadas > 0

def deletar_item_cardapio(item_id: int):
    conn = get_conexao() #type: ignore
    cursor = conn.execute("DELETE FROM cardapio WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0