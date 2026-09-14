#FETCH NO SERVER COMPONENT
async function getData() {
  const res = await fetch('https://api.exemplo.com/data', { cache: 'no-store' })
  if (!res.ok) throw new Error('Erro ao buscar dados')
  return res.json()
}
export default async function Page() {
  const data = await getData()
  return <main>{data.title}</main>
}