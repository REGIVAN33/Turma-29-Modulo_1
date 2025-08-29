idade = input("Qual sua idade? ")
idade_inteira = int(idade)

idade_minima = 16

if not idade_inteira >= idade_minima:
    print("Desculpe, você não tem idade para assistir o filme")
else:
    print("Bom filme")