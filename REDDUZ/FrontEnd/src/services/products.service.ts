import { api } from './api'


export interface Produto {
  id: number
  nome: string
  estoque_minimo: number
  quantidade_atual: number
}


export async function getProdutos(): Promise<Produto[]> {
  const response = await api.get<Produto[]>('/estoque/produtos')
  return response.data
}
