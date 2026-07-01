Sistema de Comanda Digital (MVP)

Um sistema de gerenciamento de pedidos desenvolvido como parte de um projeto de aprendizado em Python Full Stack.

Tecnologias Utilizadas:

-Backend:Python, FastAPI, Pydantic.
-Frontend:HTML5, JavaScript (Fetch API).
-Servidor:Uvicorn.

Como Rodar o Projeto:

Pré-requisitos:

- Python 3.x instalado.

Passo a Passo:

1. Clone este repositório:
   `git clone [https://github.com/Almir-07/sistema-pedidos.git]`
2. Crie e ative um ambiente virtual:
   - `python -m venv venv`
   - `.\venv\Scripts\activate` (Windows)
3. Instale as dependências:
   - `pip install fastapi uvicorn requests`
4. Inicie o servidor:
   - `uvicorn main:app --reload`
5. Abra o arquivo `index.html` no seu navegador.

Funcionalidades:

- Cadastro de pedidos via interface web.
- Listagem em tempo real dos pedidos realizados.
- Estrutura de dados validada pelo Pydantic.
- Integração via API RESTful.