from collections import namedtuple, deque, Counter, defaultdict

# NAMEDTUPLE
Ponto = namedtuple('Ponto', ['x', 'y'])
p = Ponto(10, 20)

# DEQUE (Fila dupla)
fila = deque([1, 2, 3])
fila.appendleft(0)
fila.pop()

# COUNTER
contagem = Counter(['a', 'b', 'a', 'c', 'a', 'b'])
# Counter({'a': 3, 'b': 2, 'c': 1})

# DEFAULTDICT
d = defaultdict(list)
d['chaves'].append('valor')
