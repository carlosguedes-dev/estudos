from dataclasses import dataclass, field

# DATACLASS SIMPLES
@dataclass
class Pessoa:
    nome: str
    idade: int
    ativo: bool = True
    
# DATACLASS COM FIELD (DEFAULT FACTORY)
@dataclass
class Turma:
    nome: str
    alunos: list[str] = field(default_factory=list)

p = Pessoa("Ana", 25)
