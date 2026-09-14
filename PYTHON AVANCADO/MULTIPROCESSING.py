import multiprocessing

# FUNCAO PARA O PROCESSO
def tarefa(nome):
    print(f"Processo {nome}")

# INICIANDO PROCESSOS
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=tarefa, args=('A',))
    p2 = multiprocessing.Process(target=tarefa, args=('B',))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

# POOL DE PROCESSOS
# with multiprocessing.Pool(4) as pool:
#    pool.map(tarefa, ['A', 'B', 'C', 'D'])
