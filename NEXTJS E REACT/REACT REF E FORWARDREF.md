#USEREF BÁSICO
const inputRef = useRef<HTMLInputElement>(null)
const focar = () => inputRef.current?.focus()
<input ref={inputRef} />
#FORWARDREF
const MeuInput = forwardRef<HTMLInputElement, Props>((props, ref) => (
  <input ref={ref} {...props} />
))
<MeuInput ref={inputRef} />