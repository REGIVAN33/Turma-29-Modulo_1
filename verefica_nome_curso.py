# Verificação de curso

nome = "Regivan".upper()
curso = "Python".upper()

nome_digitado = input("Digite seu nome: ").upper()
curso_digitado = input("Digite o nome do curso: ").upper()

if nome == nome_digitado and curso == curso_digitado:
    print("Bem-vindo a Tuma 29!")
else:
    print("Você não está matriculado.")