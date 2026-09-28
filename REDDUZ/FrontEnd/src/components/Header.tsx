import { Menu } from 'lucide-react'

interface HeaderProps {
  userName: string
}

export function Header({ userName }: HeaderProps) {
  return (
    <header className="relative flex items-center justify-between h-14 mb-6">
      {/* Botão menu */}
      <button className="p-2">
        <Menu className="w-6 h-6 text-gray-700" />
      </button>

      {/* Logo centralizada */}
      <div className="absolute left-1/2 -translate-x-1/2">
        <span className="text-lg font-bold text-blue-600">
          Redduz
        </span>
      </div>

      {/* Espaço à direita (equilíbrio visual) */}
      <div className="w-10" />
    </header>
  )
}
