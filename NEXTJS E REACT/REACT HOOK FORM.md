#CONFIGURAÇÃO BASICA
import { useForm } from "react-hook-form"
const { register, handleSubmit, formState: { errors } } = useForm()
const onSubmit = (data) => console.log(data)
#USO NO FORM
<form onSubmit={handleSubmit(onSubmit)}>
  <input {...register("firstName", { required: true })} />
  {errors.firstName && <span>Obrigatório</span>}
  <input type="submit" />
</form>