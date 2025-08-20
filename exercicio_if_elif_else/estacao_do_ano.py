# Peça o nome de um mês ao usuário para imprimir a estação do ano 
#Correspondente (primavera, verão, outono ou inverno).
#Outono: Abril, Maio e Junho
#Inverno: Julho, Agosto e Setembro
#Primavera : Outubro, Novembro e Dezembro
#Verão: Janeiro, Fevereiro e Março

mes = input("Digite o mês do ano: ").lower()

if mes == "Janeiro" or mes == "Fevereiro" or mes == "Março":
    estacao = "Verão"
elif mes ==  "Abril" or mes == "Maio" or "Junho":
    estacao = "Outono"
elif mes == "Julho" or "Agosto" or "Setembro":
    estacao = "Inverno" 
elif mes == "Outubro" or "Novembro" or "Dezembro":
    estacao = "Primavera" 
else:
    estacao = "Mês inválido"
print(f"O mês de {mes.capitalize()} pertence à estação: {estacao}")


