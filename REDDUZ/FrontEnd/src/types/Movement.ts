export interface Movement {
  id: number;
  produto_id: number;
  produto: string;
  tipo: "ENTRADA" | "SAIDA";
  quantidade: number;
  data: string;
}
