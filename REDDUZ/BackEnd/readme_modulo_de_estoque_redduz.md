# 📦 REDDUZ – Módulo de Estoque

## 📌 Visão Geral
O módulo de **Estoque** do projeto **REDDUZ** é responsável por gerenciar produtos, controlar quantidades disponíveis, registrar entradas e saídas e manter um histórico completo de movimentações. Este módulo foi desenvolvido como parte do MVP do sistema, utilizando **FastAPI**, **PostgreSQL** e **SQLAlchemy**.

A API segue o padrão REST e conta com documentação automática via **Swagger (OpenAPI)**.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **FastAPI** – Framework web
- **PostgreSQL** – Banco de dados relacional
- **SQLAlchemy** – ORM
- **Pydantic** – Validação e serialização de dados
- **Uvicorn** – Servidor ASGI

---

## 📂 Estrutura de Pastas (Relacionada ao Estoque)

```
app/
 ├── routes/
 │   └── estoque.py        # Rotas HTTP do módulo de estoque
 ├── schemas/
 │   └── estoque.py        # Schemas Pydantic (request/response)
 ├── database/
 │   ├── db.py             # Configuração do banco de dados
 │   ├── models.py         # Models ORM (Produto e Movimentacao)
 │   └── deps.py           # Dependência de sessão do banco
```

---

## 🧱 Models (Banco de Dados)

### Produto (`produtos`)
Representa um item controlado no estoque.

Campos:
- `id` – Identificador único
- `nome` – Nome do produto
- `estoque_minimo` – Quantidade mínima aceitável
- `quantidade_atual` – Quantidade atual em estoque

Relacionamento:
- Um produto pode possuir várias movimentações

---

### Movimentacao (`movimentacoes`)
Registra toda entrada ou saída de produtos.

Campos:
- `id`
- `produto_id` – Chave estrangeira para produtos
- `tipo` – ENTRADA ou SAIDA
- `quantidade`
- `data` – Data e hora do registro

Esse histórico é essencial para auditoria, relatórios e controle de consumo.

---

## 📐 Schemas (Pydantic)

Os schemas garantem validação dos dados, padronização das respostas e um contrato claro entre backend e frontend.

### ProdutoCreate
Utilizado para criação de produtos.

### ProdutoUpdate
Utilizado para atualização parcial de produtos.

### ProdutoResponse
Utilizado como `response_model` para padronizar as respostas.

### EntradaEstoque / SaidaEstoque
Utilizados para registrar movimentações de entrada e saída.

### MovimentacaoResponse
Define o formato de retorno do histórico de movimentações.

---

## 🌐 Rotas da API – Estoque

### GET `/estoque/produtos`
Lista todos os produtos cadastrados.

**Uso:** Exibição do estoque atual.

---

### POST `/estoque/produtos`
Cria um novo produto no estoque.

**Fluxo:**
1. Validação dos dados
2. Persistência no banco
3. Retorno do produto criado

---

### PUT `/estoque/produtos/{produto_id}`
Atualiza informações de um produto existente.

---

### DELETE `/estoque/produtos/{produto_id}`
Remove um produto do estoque.

> ⚠️ No MVP a exclusão é física. Pode evoluir para *soft delete* futuramente.

---

### POST `/estoque/entrada`
Registra entrada de produto no estoque.

**Regras:**
- Produto deve existir
- Quantidade é somada ao estoque atual
- Gera movimentação do tipo ENTRADA

---

### POST `/estoque/saida`
Registra saída de produto do estoque.

**Regras:**
- Produto deve existir
- Não permite estoque negativo
- Gera movimentação do tipo SAIDA

---

### GET `/estoque/alertas`
Lista produtos com estoque abaixo ou igual ao mínimo.

**Uso:** Alertas de reposição.

---

### GET `/estoque/movimentacoes`
Lista todo o histórico de movimentações.

**Características:**
- Ordenado por data (mais recente primeiro)
- Retorna nome do produto

---

## 🔐 Dependência de Banco de Dados

A sessão com o banco é controlada via dependência:

- `get_db()` abre a sessão
- Garante fechamento correto ao final da requisição

---

## 📊 Estado Atual do MVP

- ✅ CRUD completo de produtos
- ✅ Controle real de estoque
- ✅ Histórico de movimentações
- ✅ Alertas por estoque mínimo
- ✅ Documentação via Swagger

---

## 🚀 Próximos Passos

- Filtros por data e produto
- Relatórios de consumo
- Autenticação de usuários
- Integração com frontend
- Alertas automatizados

---

## 📄 Licença
Projeto em desenvolvimento – uso educacional e experimental.

