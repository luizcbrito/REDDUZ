import { Home, Box, Clock } from 'lucide-react'

export function BottomNavigation() {
  return (
    <nav className="absolute bottom-0 left-0 right-0 h-16 bg-white border-t flex justify-around items-center">
      <button className="flex flex-col items-center text-blue-600">
        <Home size={22} />
        <span className="text-xs">Home</span>
      </button>

      <button className="flex flex-col items-center text-gray-400">
        <Box size={22} />
        <span className="text-xs">Produtos</span>
      </button>

      <button className="flex flex-col items-center text-gray-400">
        <Clock size={22} />
        <span className="text-xs">Histórico</span>
      </button>
    </nav>
  )
}
