import type { Movement } from "../types/Movement";
import { ArrowDown, ArrowUp } from "lucide-react";

interface Props {
  movement: Movement;
  onClick?: () => void;
}

export function MovementItem({ movement, onClick }: Props) {
  const isEntrada = movement.tipo === "ENTRADA";

  return (
    <button
      onClick={onClick}
      className="w-full flex items-center justify-between p-4 rounded-xl bg-white border active:scale-[0.98] transition"
    >
      <div className="flex items-center gap-3">
        <div
          className={`p-2 rounded-lg ${isEntrada
            ? "bg-green-100 text-green-600"
            : "bg-red-100 text-red-600"
            }`}
        >
          {isEntrada ? <ArrowDown size={18} /> : <ArrowUp size={18} />}
        </div>

        <div className="text-left">
          <p className="font-medium text-gray-800">
            {movement.produto}
          </p>
          <p className="text-sm text-gray-500">
            {movement.quantidade} unidades
          </p>
        </div>
      </div>

      <div className="text-right">
        <p
          className={`text-xs font-semibold ${isEntrada ? "text-green-600" : "text-red-600"
            }`}
        >
          {movement.tipo}
        </p>
        <p className="text-xs text-gray-400">
          {new Date(movement.data).toLocaleDateString("pt-BR")}
        </p>
      </div>
    </button>
  );
}
