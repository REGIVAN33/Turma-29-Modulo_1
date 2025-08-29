frase = input("Digite uma frase ")
palavra = input("Digite uma palavra ")

if palavra in frase:
    print(f"{palavra} esta na frase")
else:
    print(f"{palavra} não tem na frase")