# Crie um programa que pede dois números e um operador matemático 
#(+, -, *, /). Para realizar a operação correta e imprimir o resultado.
# Extra: Tratar a divisão por zero!

numero1 = float(input("Digite o primeiro numero: "))
operador = input("Digite o operador (+, -, *, /): ")
numero2 = float(input("Digite o segundo numero: "))
tratar_erro = True
if operador == '+':
    resultado = numero1 + numero2
elif operador == '-':
    resultado = numero1 - numero2
elif operador == '*':
    resultado = numero1 * numero2
elif operador == '/':
    if numero2 == 0:
        print("Erro, Não é possivel dividir por zero")
        tratar_erro = False
    else:
        resultado = numero1 / numero2
else:

























    
    print("Diite um número válido")
if tratar_erro:
  print(f"O resultado é: {resultado}")