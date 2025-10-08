# 📦 API de Vendas com FastAPI

Esta é uma API simples criada com [FastAPI], que retorna informações básicas sobre vendas de produtos. A API está estruturada para fornecer:

- O número total de vendas cadastradas.
- Os detalhes de uma venda específica a partir do seu ID.

---

## 🚀 Como executar o projeto

### ✅ Pré-requisitos

- Python 3.8+
- Instalar: pip install fastapi uvicorn

# ▶️ Rodando o servidor localmente

- Salve o código em um arquivo chamado api.py

- No terminal, execute: uvicorn api:app --reload

- Acesse no navegador por exemplo: http://127.0.0.1:8000/vendas/2

# 📁 Estrutura da API


      {
      1: {"item": "refrigerante lata", "preco_unitario": 4, "quantidade": 5},
      2: {"item": "agua 2L", "preco_unitario": 15, "quantidade": 5},
      3: {"item": "suco 1L", "preco_unitario": 8, "quantidade": 2},
      }

# Testando com Postman

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/b42e7fc0-0c88-4bbe-958b-c8887f4b76b0" />

# Comandos utilizados do git.

git init - iniciar novo projeto.
git add  - adiciona arquivos.
git commit -m "commit" - commit os arquivos no histórico.
git merge - merge de ramificações.
git branch - mostra branch atual.
git checkout - muda pra essa branch.
git branch -b - cria uma nova branch.
git remote add - adiciona novo repositório remoto.
git push - manda nossas alterações locais para o repositório remoto.
git pull - pega as alterações do repositório remoto e joga pra nossa maquina.
