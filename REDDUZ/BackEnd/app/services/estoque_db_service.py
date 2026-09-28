from sqlalchemy.orm import Session
from app.database.models import Produto

def listar_produtos(db: Session):
    return db.query(Produto).all()


def criar_produto(db: Session, nome: str, estoque_minimo: float, quantidade_atual: float):
    produto = Produto(
        nome=nome,
        estoque_minimo=estoque_minimo,
        quantidade_atual=quantidade_atual
    )
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto
