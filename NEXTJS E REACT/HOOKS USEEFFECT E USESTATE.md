#USESTATE
const [count, setCount] = useState(0)
#USEEFFECT (MONTAR)
useEffect(() => {
  console.log('montou')
}, [])
#USEEFFECT (ATUALIZAR)
useEffect(() => {
  console.log('count mudou', count)
}, [count])
#USEEFFECT (DESMONTAR)
useEffect(() => {
  return () => console.log('desmontou')
}, [])