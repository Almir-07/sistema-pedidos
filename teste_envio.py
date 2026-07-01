import requests #type:ignore

url = "http://localhost:8000/pedidos/"
pedido= {
    "id": 1,
    "mesa": 5,
    "cliente": "João Silva",
    "item": "Pizza de calabresa",
    "preco": 45.50,
    "status": "Pendente"
}

resposta = requests.post(url, json=pedido)
print(resposta.json())