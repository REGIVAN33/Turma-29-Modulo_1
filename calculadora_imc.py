# caucular o IMC e imprimir o resultado na tela

nome = str(input("Digite seu nome: "))
peso = float(input("Agora digite seu peso: "))
altura = float(input("Por fim, digite sua altura: "))
seu_imc = peso / (altura * 2)

if seu_imc < 18.5 :
    print(f"{nome}, seu IMC {seu_imc:.2f} está abaixo do peso")
elif seu_imc <= 24.9 :
    print(f"{nome}, seu IMC {seu_imc:.2f} esta normal")
elif seu_imc <= 30:
    print(f"{nome}, seu IMC {seu_imc:.2f} sobrepeso")
elif seu_imc <= 35:
    print(f"{nome}, seu IMC {seu_imc:.2f} Obesidade grau I")
elif seu_imc <= 40:
    print(f"{nome}, seu IMC {seu_imc:.2f} Obesidade grau II")
else:
    print(f"{nome}, seu IMC {seu_imc:.2f} Obesidade grau III (Mórbida)")
    
