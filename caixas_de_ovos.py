# Um fazendeiro precisa empacotar ovos, Ele têm 145 ovos no total
# As caixas de ovos são para 12 unidades. Ele quer saber
# quantas caixas completas ele consegue encher?
# Quantos ovos sobram no final?

ovos = 145
caixas_de_ovos = 12
caixas_cheias = ovos // caixas_de_ovos
sobra_final = ovos % caixas_de_ovos
print(f"145 Ovos dá para {caixas_cheias} caixas com 12, e sobra(m) {sobra_final} ovo(s)")
