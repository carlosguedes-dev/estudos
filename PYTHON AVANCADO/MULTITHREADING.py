import threading

# FUNCAO PARA THREAD
def tarefa(nome):
    print(f"Thread {nome}")

# INICIANDO THREADS
t1 = threading.Thread(target=tarefa, args=('1',))
t2 = threading.Thread(target=tarefa, args=('2',))

t1.start()
t2.start()

t1.join()
t2.join()
