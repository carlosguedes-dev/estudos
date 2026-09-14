# USANDO WITH (ARQUIVOS)
with open('teste.txt', 'w') as f:
    f.write('ola')

# CONTEXT MANAGER COM CLASS
class MeuContexto:
    def __enter__(self):
        print("Entrou")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saiu")

# CONTEXT MANAGER COM DECORATOR
from contextlib import contextmanager

@contextmanager
def meu_contexto_func():
    print("Entrou")
    yield
    print("Saiu")
