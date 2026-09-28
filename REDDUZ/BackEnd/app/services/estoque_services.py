# app/services/estoque_service.py

estoque = {
    "Arroz": {
        "estoque_atual": 20,
        "estoque_minimo": 10
    },
    "Feijão": {
        "estoque_atual": 5,
        "estoque_minimo": 8
    }
}

movimentacoes = []


def entrada_produto(produto: str, quantidade: float):
    if produto not in estoque:
        raise ValueError("Produto não encontrado")

    estoque[produto]["estoque_atual"] += quantidade

    movimentacoes.append({
        "produto": produto,
        "tipo": "entrada",
        "quantidade": quantidade
    })


def saida_produto(produto: str, quantidade: float):
    if produto not in estoque:
        raise ValueError("Produto não encontrado")

    if estoque[produto]["estoque_atual"] < quantidade:
        raise ValueError("Estoque insuficiente")

    estoque[produto]["estoque_atual"] -= quantidade

    movimentacoes.append({
        "produto": produto,
        "tipo": "saida",
        "quantidade": quantidade
    })


def produtos_em_alerta():
    alertas = []

    for produto, dados in estoque.items():
        if dados["estoque_atual"] <= dados["estoque_minimo"]:
            alertas.append(produto)

    return alertas
