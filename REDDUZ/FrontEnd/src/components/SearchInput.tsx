import { Search } from 'lucide-react'

interface SearchInputProps {
  value: string
  onChange: (value: string) => void
  placeholder?: string
}

export function SearchInput({
  value,
  onChange,
  placeholder = 'Pesquisar movimentações...',
}: SearchInputProps) {
  return (
    <div className="flex items-center gap-2 px-4 py-3 mb-4 bg-white rounded-xl border border-gray-200">
      <Search size={18} className="text-gray-400" />

      <input
        type="text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder={placeholder}
        className="flex-1 bg-transparent outline-none text-sm text-gray-700 placeholder:text-gray-400"
      />
    </div>
  )
}
