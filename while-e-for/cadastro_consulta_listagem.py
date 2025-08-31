def cadastramento():
    """
    Função para realizar o cadastramento.
    """
    print("--- Opção: Cadastramento ---")
    print("Realizando o cadastramento de uma nova consulta...")
    # Aqui entraria o código para cadastrar
    input("Pressione <ENTER> para continuar.")

def consulta():
    """
    Função para realizar a consulta.
    """
    print("--- Opção: Consulta ---")
    print("Realizando uma consulta...")
    # Aqui entraria o código para consultar
    input("Pressione <ENTER> para continuar.")

def listagem(tipo_relatorio):
    """
    Função para gerar uma listagem.

    Args:
        tipo_relatorio (int): O tipo de relatório a ser gerado (1 para resumido, 2 para detalhado).
    """
    print("--- Opção: Listagem ---")
    print("Gerando relatório...")
    if tipo_relatorio == 1:
        print("Gerando relatório resumido.")
    else:
        print("Gerando relatório detalhado.")
    
    print("O relatório foi gerado com sucesso!")
    input("Pressione <ENTER> para continuar.")

def exibir_menu():
    """
    Função para exibir o menu de opções.
    """
    print("====================================")
    print("         MENU PRINCIPAL           ")
    print("====================================")
    print(" 1 - Cadastramento")
    print(" 2 - Consulta")
    print(" 3 - Listagem")
    print(" 4 - Fim")
    print("====================================")

def main():
    """
    Função principal que gerencia o fluxo do programa.
    """
    opcao = 0
    while opcao != 4:
        exibir_menu()
        try:
            opcao = int(input("Escolha a sua opção: "))
            if opcao == 1:
                cadastramento()
            elif opcao == 2:
                consulta()
            elif opcao == 3:
                # Chama a listagem com um tipo de relatório fixo. Você pode modificar isso para pedir ao usuário o tipo de relatório.
                listagem(2)
            elif opcao == 4:
                print("Encerrando o programa. Até mais!")
            else:
                print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# Chama a função principal para iniciar o programa
if __name__ == "__main__":
    main()