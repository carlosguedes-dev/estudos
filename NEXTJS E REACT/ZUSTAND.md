#CRIAR STORE ZUSTAND
import create from 'zustand'
export const useStore = create((set) => ({
  bears: 0,
  increasePopulation: () => set((state) => ({ bears: state.bears + 1 })),
  removeAllBears: () => set({ bears: 0 }),
}))
#USAR STORE
const bears = useStore((state) => state.bears)
const increase = useStore((state) => state.increasePopulation)