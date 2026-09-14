from typing import List, Dict, Optional, Union, Callable

# TIPAGEM BASICA
nome: str = "Maria"
idade: int = 30

# LISTAS E DICIONARIOS
numeros: List[int] = [1, 2, 3]
dados: Dict[str, Union[int, str]] = {"id": 1, "nome": "João"}

# OPTIONAL
def busca(id: int) -> Optional[str]:
    return None

# CALLABLE
def executa(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)
