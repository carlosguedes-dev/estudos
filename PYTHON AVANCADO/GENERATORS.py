# FUNCAO GENERATOR
def contador(maximo):
    n = 0
    while n < maximo:
        yield n
        n += 1

# GENERATOR EXPRESSION
quadrados = (x**2 for x in range(10))

# USO
for i in contador(5):
    print(i)
