from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class EntradaEstoque(BaseModel):
    produto: str = Field(..., example="Arroz")
    quantidade: float = Field(..., gt=0, example=10)

class SaidaEstoque(BaseModel):
    produto: str = Field(..., example="Arroz")
    quantidade: float = Field(..., gt=0, example=2)

class ProdutoCreate(BaseModel):
    nome: str
    estoque_minimo: float
    quantidade_atual: float

class ProdutoUpdate(BaseModel):
    nome: Optional[str] = None
    estoque_minimo: Optional[float] = None
    quantidade_atual: Optional[float] = None


class MovimentacaoResponse(BaseModel):
    id: int
    produto_id: int
    produto: str
    tipo: str
    quantidade: float
    data: datetime

    class Config:
        from_attributes = True

class ProdutoResponse(BaseModel):
    id: int
    nome: str
    estoque_minimo: float
    quantidade_atual: float

    class Config:
        from_attributes = True  # 👈 MUITO IMPORTANTE
