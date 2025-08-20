# caucular o IMC e imprimir o resultado na tela

nome = str(input("Digite seu nome: "))
peso = float(input("Agora digite seu peso: "))
altura = float(input("Por fim, digite sua altura: "))
seu_imc = peso / (altura * 2)

if seu_imc <= 18.5 :
    print(f"{nome}, seu IMC {seu_imc:.2f} está abaixo do peso")
elif seu_imc <= 24.9 :
    print(f"{nome}, seu IMC {seu_imc:.2f} esta normal")
else :
    print(f"{nome}, seu IMC {seu_imc:.2f} está acima do peso")
    
