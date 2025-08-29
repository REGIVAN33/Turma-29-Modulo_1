# Crie um programa que pede dois números e um operador matemático 
#(+, -, *, /). Para realizar a operação correta e imprimir o resultado.
# Extra: Tratar a divisão por zero!

numero1 = float(input("Digite o primeiro numero: "))
operador = input("Digite o operador (+, -, *, /): ")
numero2 = float(input("Digite o segundo numero: "))
<<<<<<< HEAD

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
=======
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
>>>>>>> 84d442afcc04c69ccd62a9cff89d462edb7894b3
