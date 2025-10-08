from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {"item": "refrigerante lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "agua 2L", "preco_unitario": 15, "quantidade": 5},
    3: {"item": "suco 1L", "preco_unitario": 8, "quantidade": 2},
}

@app.get("/")
def home():
    return {"Vendas": len(vendas)}

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    return vendas[id_venda]