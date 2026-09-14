#NEXT/IMAGE
import Image from 'next/image'
<Image src="/logo.png" alt="Logo" width={500} height={300} priority />
#NEXT/LINK
import Link from 'next/link'
<Link href="/sobre" prefetch={false}>Sobre</Link>