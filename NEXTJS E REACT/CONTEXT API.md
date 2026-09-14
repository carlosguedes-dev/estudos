#CRIAR CONTEXT
import { createContext, useContext, useState } from 'react'
export const ThemeContext = createContext(null)
export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState('light')
  return <ThemeContext.Provider value={{ theme, setTheme }}>{children}</ThemeContext.Provider>
}
#USAR CONTEXT
const { theme, setTheme } = useContext(ThemeContext)