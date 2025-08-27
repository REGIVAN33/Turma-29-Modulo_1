senha = input("Crie uma senha: ")
comprimento_senha = len(senha)

if comprimento_senha >= 8:
    print("Sucesso")
else:
    print(f"Erro, Senha muito pequena, {comprimento_senha} caracter")
