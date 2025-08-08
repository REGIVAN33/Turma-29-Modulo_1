def calculadora():
    # Loop principal para que a calculadora rode continuamente
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            operacao = input("Digite a operação (+, -, *, /) ou 'sair' para fechar: ")

            # Verificação para sair do programa
            if operacao.lower() == 'sair':
                print("Calculadora encerrada. Até mais!")
                break

            num2 = float(input("Digite o segundo número: "))

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                    continue  # Volta para o início do loop
                else:
                    resultado = num1 / num2
            else:
                print("Operação inválida.")
                continue # Volta para o início do loop

            print(f"O resultado é: {resultado}")

        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")
        
# Chama a função para iniciar a calculadora
calculadora()