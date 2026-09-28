type MobileContainerProps = {
  children: React.ReactNode
}

export function MobileContainer({ children }: MobileContainerProps) {
  return (
    <div className="min-h-screen bg-gray-300 flex justify-center">
      <div className="w-full max-w-[390px] bg-gray-100 min-h-screen relative">
        {children}
      </div>
    </div>
  )
}
