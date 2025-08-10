#Calculadoa de idade de uma pessoa a partir do ano de nascimento.

ano_de_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade_calculada = ano_atual - ano_de_nascimento
print(f"Sua idade é: {idade_calculada}")
