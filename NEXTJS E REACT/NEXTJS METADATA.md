#METADATA ESTATICO
export const metadata: Metadata = {
  title: 'Meu App',
  description: 'App criado em Next.js',
}
#METADATA DINAMICO
export async function generateMetadata({ params }): Promise<Metadata> {
  const product = await fetchProduct(params.id)
  return { title: product.title }
}