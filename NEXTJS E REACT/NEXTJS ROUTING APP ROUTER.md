#ROTA DINAMICA (app/blog/[slug]/page.tsx)
export default function Page({ params }: { params: { slug: string } }) {
  return <div>Post: {params.slug}</div>
}
#CATCH-ALL (app/shop/[...slug]/page.tsx)
export default function Page({ params }: { params: { slug: string[] } }) {
  return <div>Categorias: {params.slug.join(', ')}</div>
}