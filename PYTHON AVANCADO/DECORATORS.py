# DECORATOR SIMPLES
def meu_decorator(func):
    def wrapper(*args, **kwargs):
        print("Antes")
        resultado = func(*args, **kwargs)
        print("Depois")
        return resultado
    return wrapper

@meu_decorator
def ola():
    print("Olá")

# DECORATOR COM ARGUMENTOS
def repete(vezes):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(vezes):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repete(3)
def oi():
    print("Oi")
