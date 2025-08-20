# Peça 4 notas de um aluno. Se a média for maior ou igual a 7 escreva:
# "Aprovado.” 
# Se for menor que 7 mas maior ou igual a 5, escreva: 
#“Em Recuperação” 
#Se for menor que 5 escreva: 
#“Reprovado” 

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print("Aprovado")
elif media >= 5 :
    print("Em recuperação")
else:
    print("reprovado")