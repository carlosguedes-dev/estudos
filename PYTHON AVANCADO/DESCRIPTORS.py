# DESCRIPTOR CLASS
class ValidarTipo:
    def __init__(self, nome, tipo_esperado):
        self.nome = nome
        self.tipo = tipo_esperado
        
    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.nome)
        
    def __set__(self, obj, valor):
        if not isinstance(valor, self.tipo):
            raise TypeError(f"Esperado {self.tipo}")
        obj.__dict__[self.nome] = valor

class Exemplo:
    idade = ValidarTipo('idade', int)

e = Exemplo()
e.idade = 20
