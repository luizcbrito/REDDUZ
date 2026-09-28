import { api } from "./api";
import type { Movement } from "../types/Movement";

interface GetMovimentacoesParams {
  nome_produto?: string;
}

export const getMovimentacoes = async (
  params?: GetMovimentacoesParams
): Promise<Movement[]> => {
  const response = await api.get("/estoque/movimentacoes", {
    params,
  });

  return response.data;
};
