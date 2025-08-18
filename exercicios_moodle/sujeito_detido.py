# Um suspeito foi detido preventivamente
# em uma terça-feira e seria julgado depois
# de 50 dias. O seu julgamento aconteceu em uma:
# a) Segunda-feira.
# b) Terça-feira.
# c) Quarta-feira.
# d) Quinta-feira.
# e) Sexta-feira. 


dias_da_semana = {
    0: "Domingo",
    1: "Segunda-feira",
    2: "Terça-feira",
    3: "Quarta-feira",
    4: "Quinta-feira",
    5: "Sexta-feira",
    6: "Sábado"
}

dia_detencao = 2

dias_ate_julgamento = 50

resto_da_divisao = dias_ate_julgamento % 7

dia_do_julgamento = (dia_detencao + resto_da_divisao) % 7

print(f"O suspeito foi detido em uma: {dias_da_semana[dia_detencao]}")
print(f"O julgamento será em uma: {dias_da_semana[dia_do_julgamento]}")