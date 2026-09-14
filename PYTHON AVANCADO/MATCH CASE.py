# PATTERN MATCHING (PYTHON 3.10+)
comando = "sair"

match comando:
    case "iniciar":
        print("Iniciando")
    case "parar":
        print("Parando")
    case "sair" | "exit":
        print("Saindo")
    case _:
        print("Comando inválido")

# MATCH COM ESTRUTURAS
dados = {"tipo": "usuario", "id": 123}

match dados:
    case {"tipo": "usuario", "id": id_usuario}:
        print(f"Usuário {id_usuario}")
