# METACLASS BASICA
class MinhaMeta(type):
    def __new__(cls, name, bases, dct):
        dct['atributo_injetado'] = 100
        return super().__new__(cls, name, bases, dct)

# USANDO A METACLASS
class MinhaClasse(metaclass=MinhaMeta):
    pass

print(MinhaClasse.atributo_injetado)
