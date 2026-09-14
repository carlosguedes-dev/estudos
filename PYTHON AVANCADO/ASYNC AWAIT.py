import asyncio

# COROUTINE BASICA
async def faz_algo():
    print("Iniciando")
    await asyncio.sleep(1)
    print("Terminando")

# EXECUTANDO
# asyncio.run(faz_algo())

# CONCORRENCIA
async def principal():
    tarefa1 = asyncio.create_task(faz_algo())
    tarefa2 = asyncio.create_task(faz_algo())
    await tarefa1
    await tarefa2
