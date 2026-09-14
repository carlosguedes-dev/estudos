import math

# BASEADO NO MEU PROJETO senhas-logaritmo
def calcular_entropia(senha):
    tamanho = len(senha)
    # letras, nums, especiais = ~94 caracteres
    possibilidades = 94
    entropia = tamanho * math.log2(possibilidades)
    return entropia

print(calcular_entropia("MinhaSenhaForte!"))
