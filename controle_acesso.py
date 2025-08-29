# Conrole de acesso a Evento
lista_vip = "sim"
ingresso = "sim"

sua_lista_vip = input("Você está na lista vip? 'sim, ou não:' ")
seu_ingresso = input(" Você tem ingresso? 'sim ou não': ")

if sua_lista_vip == lista_vip or seu_ingresso == lista_vip:
    print("Entrada permitida")
else:
    print("Entrada negada")
