# Pedindo ao usuário para digitar o primeiro número
num1 = float(input("Digite o primeiro número: "))

# Pedindo a operação
operacao = input("Digite a operação (+, -, *, /): ")

# Pedindo ao usuário para digitar o segundo número
num2 = float(input("Digite o segundo número: "))

# Executando o cálculo com base na operação
if operacao == '+':
    resultado = num1 + num2
    print(f"O resultado é: {resultado}")
elif operacao == '-':
    resultado = num1 - num2
    print(f"O resultado é: {resultado}")
elif operacao == '*':
    resultado = num1 * num2
    print(f"O resultado é: {resultado}")
elif operacao == '/':
    # Adicionando uma verificação para evitar divisão por zero
    if num2 == 0:
        print("Erro: Divisão por zero não é permitida.")
    else:
        resultado = num1 / num2
        print(f"O resultado é: {resultado}")
else: