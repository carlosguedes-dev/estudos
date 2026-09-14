#SERVER ACTION
'use server'
export async function createPost(formData: FormData) {
  const title = formData.get('title')
  await db.post.create({ data: { title } })
  revalidatePath('/posts')
}
#USAR NO CLIENT
<form action={createPost}>
  <input name="title" />
  <button type="submit">Enviar</button>
</form>