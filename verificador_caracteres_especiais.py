lista = ("@" or "!" or "#" or "$")
nome_usuario = input("Crie um nome de usuário ").lower()

if  lista not in nome_usuario:
    print("Nome válido")
else:
    print("Nome de usuário não pode conter caracteres especiais")
