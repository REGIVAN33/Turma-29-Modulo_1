# Crie um programa que pede dois números e um operador matemático 
#(+, -, *, /). Para realizar a operação correta e imprimir o resultado.
# Extra: Tratar a divisão por zero!

numero1 = float(input("Digite o primeiro numero: "))
operador = input("Digite o operador (+, -, *, /): ")
numero2 = float(input("Digite o segundo numero: "))

if operador == '+':
    resultado = numero1 + numero2
    print(resultado)
elif operador == '-':
    resultado = numero1 - numero2
    print(resultado)
elif operador == '*':
    resultado = numero1 * numero2
    print(resultado)
elif operador == '/':
    if numero2 == 0:
        print("Erro, Não é possivel dividir por zero")
    else:
        resultado = numero1 / numero2
        print(resultado)
else:
    print("Você não digitou um número válido")
