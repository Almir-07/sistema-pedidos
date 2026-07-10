import sqlite3
from models.pedido import Pedido #type: ignore

# Função para conectar ao banco de dados
def get_conexao():
    conn = sqlite3.connect("pedidos.db", check_same_thread=False, timeout=10.0)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabela():
    conn = get_conexao()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY,
            mesa INTEGER,
            cliente TEXT,
            item TEXT,
            preco REAL,
            status TEXT
        )
    """)
    
    conn.execute("""
        CREATE TABLE IF NOT EXISTS cardapio (
            id INTEGER PRIMARY KEY,
            nome TEXT UNIQUE,
            preco REAL
        )
    """)
    
    conn.commit()
    conn.close()

criar_tabela()

def listar_todos():
    conn = get_conexao()
    cursor = conn.execute("SELECT * FROM pedidos")
    linhas = cursor.fetchall()
    conn.close()
    return [dict(linha) for linha in linhas]

def criar(pedido: Pedido):
    conn = get_conexao()
    cursor = conn.execute(
        "INSERT INTO pedidos (mesa, cliente, item, preco, status) VALUES (?, ?, ?, ?, ?)",
        (pedido.mesa, pedido.cliente, pedido.item, pedido.preco, pedido.status)
    )
    pedido.id = cursor.lastrowid
    conn.commit()
    conn.close()
    return pedido

def atualizar(pedido_id: int, dados_atualizados: Pedido):
    conn = get_conexao()
    cursor = conn.execute("SELECT id FROM pedidos WHERE id = ?", (pedido_id,))
    if not cursor.fetchone():
        conn.close()
        return None
        
    conn.execute(
        "UPDATE pedidos SET mesa=?, cliente=?, item=?, preco=?, status=? WHERE id=?",
        (dados_atualizados.mesa, dados_atualizados.cliente, dados_atualizados.item, dados_atualizados.preco, dados_atualizados.status, pedido_id)
    )
    conn.commit()
    conn.close()
    return dados_atualizados

def deletar(pedido_id: int):
    conn = get_conexao()
    cursor = conn.execute("SELECT id FROM pedidos WHERE id = ?", (pedido_id,))
    if not cursor.fetchone():
        conn.close()
        return None
        
    conn.execute("DELETE FROM pedidos WHERE id = ?", (pedido_id,))
    conn.commit()
    conn.close()
    return True

def deletar_item_cardapio(item_id: int):
    conn = get_conexao()
    try:
        cursor = conn.execute("DELETE FROM cardapio WHERE id = ?", (item_id,))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"ERRO NO BANCO: {e}")
        return False
    finally:
        conn.close()

def listar_cardapio():
    conn = get_conexao()
    cursor = conn.execute("SELECT * FROM cardapio")
    linhas = cursor.fetchall()
    conn.close()
    return [dict(linha) for linha in linhas]

def adicionar_ao_cardapio(nome: str, preco: float):
    conn = get_conexao()
    try:
        conn.execute("INSERT INTO cardapio (nome, preco) VALUES (?, ?)", (nome, preco))
        conn.commit()
    except sqlite3.IntegrityError:
        pass 
    finally:
        conn.close()