import { Header } from '../components/Header'
import { StatusCard } from '../components/StatusCard'
import { MovementItem } from '../components/MovementItem'
import { BottomNavigation } from '../components/BottomNavigation'
import { MobileContainer } from '../components/MobileContainer'
import { useState, useEffect } from 'react'
import { SearchInput } from '../components/SearchInput'
import { getProdutos } from '../services/products.service'
import { getAlertas } from '../services/alerts.service'
import { getMovimentacoes } from "../services/movements.service";
import type { Movement } from "../types/Movement"





export default function Home() {
  const [search, setSearch] = useState('')
  const [movements, setMovements] = useState<Movement[]>([]);
  const [loadingMovements, setLoadingMovements] = useState(false);
  const [totalProdutos, setTotalProdutos] = useState<number>(0)
  const [totalAlertas, setTotalAlertas] = useState<number>(0);
  const [movimentacoes, setMovimentacoes] = useState<Movement[]>([]);

  async function carregarMovimentacoes(nomeProduto?: string) {
    try {
      setLoadingMovements(true);

      const data = await getMovimentacoes(
        nomeProduto
          ? { nome_produto: nomeProduto }
          : undefined
      );

      setMovements(data);
    } catch (error) {
      console.error("Erro ao carregar movimentações", error);
    } finally {
      setLoadingMovements(false);
    }
  }



  const carregarAlertas = async () => {
    try {
      const data = await getAlertas();

      const quantidadeAlertas = data.produtos_em_alerta.length;

      setTotalAlertas(quantidadeAlertas);
    } catch (error) {
      console.error("Erro ao carregar alertas", error);
    }
  };



  useEffect(() => {
    async function carregarProdutos() {
      try {
        const produtos = await getProdutos()
        console.log('Produtos recebidos:', produtos) // 👈
        setTotalProdutos(produtos.length)
      } catch (error) {
        console.error('Erro ao carregar produtos', error)
      }
    }
    carregarMovimentacoes(search)
    carregarAlertas();
    carregarProdutos()
  }, [search])


  return (
    <MobileContainer>
      <div className="p-4 pb-24">
        <Header userName="Claudio" />
        <div className="mb-6">
          <h1 className="text-lg font-semibold text-gray-800">
            Olá, Claudio 👋
          </h1>
          <p className="text-sm text-gray-500">
            Bem-vindo.
          </p>
        </div>


        <section className="grid gap-4 mb-6">
          <StatusCard
            title="Produtos cadastrados"
            value={totalProdutos}
            color="blue"
          />


          <StatusCard
            title="Alertas"
            value={totalAlertas}
            color="red"
          />




        </section>

        <section>
          <h2 className="mb-3 text-lg font-semibold text-gray-700">
            Movimentações Recentes
          </h2>
          <SearchInput
            value={search}
            onChange={setSearch}
          />

          <ul className="space-y-3">
            {loadingMovements && (
              <p className="text-sm text-gray-400">
                Carregando movimentações...
              </p>
            )}

            {!loadingMovements && movements.length === 0 && (
              <p className="text-sm text-gray-400">
                Nenhuma movimentação encontrada
              </p>
            )}

            {movements.map((movement) => (
              <MovementItem
                key={movement.id}
                movement={movement}
              />
            ))}
          </ul>

        </section>
        <BottomNavigation />
      </div>
    </MobileContainer>
  )
}
