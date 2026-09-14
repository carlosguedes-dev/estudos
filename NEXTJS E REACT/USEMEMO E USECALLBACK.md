#USEMEMO
const calculoCaro = useMemo(() => {
  return lista.filter(item => item.ativo)
}, [lista])
#USECALLBACK
const handleClick = useCallback(() => {
  console.log('clicou', id)
}, [id])