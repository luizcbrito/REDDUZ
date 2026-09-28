import { ChevronRight, Box, AlertTriangle } from 'lucide-react'

interface StatusCardProps {
  title: string
  value: number
  color?: 'blue' | 'red'
}

export function StatusCard({
  title,
  value,
  color = 'blue',
}: StatusCardProps) {
  const isAlert = color === 'red'

  return (
    <button
      className={`
        w-full flex items-center justify-between p-4 rounded-xl
        active:scale-[0.98] transition shadow-sm
        ${isAlert
          ? 'bg-red-300 text-red-900'
          : 'bg-blue-300 text-blue-900'
        }
      `}
    >
      <div className="flex items-center gap-3">
        <div
          className={`
            p-2 rounded-lg bg-white/40
            ${isAlert ? 'text-red-800' : 'text-blue-800'}
          `}
        >
          {isAlert ? (
            <AlertTriangle size={20} />
          ) : (
            <Box size={20} />
          )}
        </div>

        <div className="text-left">
          <p className="text-sm opacity-80">{title}</p>
          <p className="text-xl font-bold">{value}</p>
        </div>
      </div>

      <ChevronRight className="opacity-70" />
    </button>
  )
}
