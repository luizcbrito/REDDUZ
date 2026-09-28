import { api } from "./api";

export const getAlertas = async () => {
  const response = await api.get("/estoque/alertas");
  return response.data;
};
