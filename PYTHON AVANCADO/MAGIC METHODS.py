# METODOS ESPECIAIS COMUNS
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
        
    def __add__(self, outro):
        return Ponto(self.x + outro.x, self.y + outro.y)
        
    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y

p1 = Ponto(1, 2)
p2 = Ponto(3, 4)
print(p1 + p2)
