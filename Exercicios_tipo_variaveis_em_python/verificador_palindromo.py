palavra = input("Digite uma palavra ").lower()
palavra_lida = palavra[-1::-1]

if palavra == palavra_lida:
    print(f"{palavra} é um palíndromo")
else:
    print("A palavra não é um palíndromo")