from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database.deps import get_db
from app.database.models import Produto, Movimentacao
from app.schemas.estoque import (
    EntradaEstoque,
    SaidaEstoque,
    ProdutoCreate
)

from typing import List
from app.schemas.estoque import ProdutoResponse

from typing import List, Optional
from fastapi import Query

router = APIRouter(prefix="/estoque", tags=["Estoque"])


@router.get("/produtos", response_model=List[ProdutoResponse])
def listar_produtos(
    nome: Optional[str] = Query(None, description="Filtrar por nome do produto"),
    abaixo_minimo: Optional[bool] = Query(
        None, description="Filtrar produtos abaixo do estoque mínimo"
    ),
    quantidade_min: Optional[float] = Query(
        None, description="Quantidade mínima em estoque"
    ),
    quantidade_max: Optional[float] = Query(
        None, description="Quantidade máxima em estoque"
    ),
    db: Session = Depends(get_db)
):
    query = db.query(Produto)

    if nome:
        query = query.filter(Produto.nome.ilike(f"%{nome}%"))

    if abaixo_minimo is True:
        query = query.filter(Produto.quantidade_atual <= Produto.estoque_minimo)

    if quantidade_min is not None:
        query = query.filter(Produto.quantidade_atual >= quantidade_min)

    if quantidade_max is not None:
        query = query.filter(Produto.quantidade_atual <= quantidade_max)

    return query.all()


@router.post("/produtos")
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    novo = Produto(
        nome=produto.nome,
        estoque_minimo=produto.estoque_minimo,
        quantidade_atual=produto.quantidade_atual
    )
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@router.post("/entrada")
def entrada_estoque(dado: EntradaEstoque, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.nome == dado.produto).first()

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    produto.quantidade_atual += dado.quantidade

    movimentacao = Movimentacao(
        produto_id=produto.id,
        tipo="ENTRADA",
        quantidade=dado.quantidade
    )

    db.add(movimentacao)
    db.commit()

    return {"mensagem": "Entrada registrada com sucesso"}


@router.post("/saida")
def saida_estoque(dado: SaidaEstoque, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.nome == dado.produto).first()

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    if produto.quantidade_atual < dado.quantidade:
        raise HTTPException(status_code=400, detail="Estoque insuficiente")

    produto.quantidade_atual -= dado.quantidade

    movimentacao = Movimentacao(
        produto_id=produto.id,
        tipo="SAIDA",
        quantidade=dado.quantidade
    )

    db.add(movimentacao)
    db.commit()

    return {"mensagem": "Saída registrada com sucesso"}


@router.get("/alertas")
def alertas(db: Session = Depends(get_db)):
    produtos = db.query(Produto).filter(
        Produto.quantidade_atual <= Produto.estoque_minimo
    ).all()

    return {"produtos_em_alerta": produtos}


@router.delete("/produtos/{produto_id}")
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    db.delete(produto)
    db.commit()

    return {"mensagem": "Produto deletado com sucesso"}

from app.schemas.estoque import ProdutoUpdate

@router.put("/produtos/{produto_id}")
def atualizar_produto(
    produto_id: int,
    dados: ProdutoUpdate,
    db: Session = Depends(get_db)
):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    if dados.nome is not None:
        produto.nome = dados.nome

    if dados.estoque_minimo is not None:
        produto.estoque_minimo = dados.estoque_minimo

    if dados.quantidade_atual is not None:
        produto.quantidade_atual = dados.quantidade_atual

    db.commit()
    db.refresh(produto)

    return produto


from typing import List
from app.schemas.estoque import MovimentacaoResponse


# filtro da movimentações
from typing import Optional, List
from datetime import date, datetime
from sqlalchemy.orm import Session
from fastapi import Depends, Query

@router.get(
    "/movimentacoes",
    response_model=List[MovimentacaoResponse]
)
def listar_movimentacoes(
    db: Session = Depends(get_db),
    produto_id: Optional[int] = Query(None),
    nome_produto: Optional[str] = Query(None),
    tipo: Optional[str] = Query(None),
    data_inicio: Optional[date] = Query(None),
    data_fim: Optional[date] = Query(None),
):
    query = (
        db.query(Movimentacao)
        .join(Produto)
        .order_by(Movimentacao.data.desc())
    )

    # 🔹 filtro por ID do produto
    if produto_id:
        query = query.filter(Movimentacao.produto_id == produto_id)

    # 🔹 filtro por nome do produto (LIKE / ILIKE)
    if nome_produto:
        query = query.filter(Produto.nome.ilike(f"%{nome_produto}%"))

    # 🔹 filtro por tipo
    if tipo:
         tipo = tipo.strip().upper()

    # 🔹 filtro por data início
    if data_inicio:
        query = query.filter(
            Movimentacao.data >= datetime.combine(
                data_inicio, datetime.min.time()
            )
        )

    # 🔹 filtro por data fim
    if data_fim:
        query = query.filter(
            Movimentacao.data <= datetime.combine(
                data_fim, datetime.max.time()
            )
        )

    movimentacoes = query.all()

    return [
        MovimentacaoResponse(
            id=m.id,
            produto_id=m.produto_id,
            produto=m.produto.nome,
            tipo=m.tipo,
            quantidade=m.quantidade,
            data=m.data,
        )
        for m in movimentacoes
    ]
